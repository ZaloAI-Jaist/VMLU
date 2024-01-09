import pandas as pd
import numpy as np
import torch
import json
import glob
import logging  
import os
import argparse
import time

from transformers import AutoModelForCausalLM, BitsAndBytesConfig, AutoTokenizer, AutoConfig
from string import Template
from pathlib import Path
from tqdm import tqdm

import warnings
warnings.simplefilter("ignore")

def main(args):
    llm = args.llm
    device = args.device
    folder = args.folder

    path = llm.replace('/', '-')

    ## create directory
    directory_path = './logs'
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    # Configure logging
    logging.basicConfig(filename=f"./logs/{path}.log", level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
    logging.info(f'Model name: {llm}')

    config = AutoConfig.from_pretrained(llm, trust_remote_code=True)  
    config.init_device = device
    # config.attn_config['attn_impl'] = 'triton' # Enable if "triton" installed!
    
    model = AutoModelForCausalLM.from_pretrained(  
        llm, config=config, torch_dtype=torch.bfloat16, trust_remote_code=True  
        )
    model.to(device)
    model.config.use_cache = False
    if 'sealion' in llm or 'Qwen' in llm:
        tokenizer = AutoTokenizer.from_pretrained(llm, trust_remote_code=True)
    else:
        tokenizer = AutoTokenizer.from_pretrained(llm)

    # Create empty lists to store data
    ids = []
    questions = []
    choices_A = []
    choices_B = []
    choices_C = []
    choices_D = []
    choices_E = []

    # Read JSONL files
    data_path = Path(folder)
    jsonl_files = list(data_path.glob('test.jsonl'))

    for file in jsonl_files:
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                data = json.loads(line)
                ids.append(data["id"])
                questions.append(data["question"])
                choices = data["choices"]
                try:
                    choices_A.append(choices[0])
                except:
                    choices_A.append('')
                try:
                    choices_B.append(choices[1])
                except:
                    choices_B.append('')
                try:
                    choices_C.append(choices[2])
                except:
                    choices_C.append('')
                try:
                    choices_D.append(choices[3])
                except:
                    choices_D.append('')
                try:
                    choices_E.append(choices[4])
                except:
                    choices_E.append('')

    # Create a DataFrame
    df = pd.DataFrame({
        "id": ids,
        "prompt": questions,
        "A": choices_A,
        "B": choices_B,
        "C": choices_C,
        "D": choices_D,
        "E": choices_E
    })
    logging.info(df.head())

    preamble = \
        'Chỉ đưa ra chữ cái đứng trước câu trả lời đúng (A, B, C, D hoặc E) của câu hỏi trắc nghiệm sau: '

    template = Template('$preamble\n\n$prompt\n\n $a\n $b\n $c\n $d\n $e\nĐáp án:')

    def format_input(df, idx):
        prompt = df.loc[idx, 'prompt']
        a = df.loc[idx, 'A']
        b = df.loc[idx, 'B']
        c = df.loc[idx, 'C']
        d = df.loc[idx, 'D']
        e = df.loc[idx, 'E']

        input_text = template.substitute(
            preamble=preamble, prompt=prompt, a=a, b=b, c=c, d=d, e=e)
        
        return input_text

    # Test a toy example
    if 'falcon' in llm:
        inputs = tokenizer(format_input(df, 0), return_tensors="pt", return_token_type_ids=False).to(device)
        outputs = model.generate(**inputs, pad_token_id=tokenizer.eos_token_id, max_new_tokens=1)
    elif 'sealion' in llm:
        inputs = tokenizer(format_input(df, 0), return_tensors="pt").to(device)
        outputs = model.generate(inputs["input_ids"], max_new_tokens=1)
    else:
        inputs = tokenizer(format_input(df, 0), return_tensors="pt").to(device)
        outputs = model.generate(**inputs, max_new_tokens=1)

    answer = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    logging.info('Contruct a toy eg')
    logging.info("Generated answer: %s", answer)

    answers = []

    start = time.time()
    for idx in tqdm(df.index):
        if 'falcon' in llm:
            inputs = tokenizer(format_input(df, idx), return_tensors="pt", return_token_type_ids=False).to(device)
            outputs = model.generate(**inputs, pad_token_id=tokenizer.eos_token_id, max_new_tokens=1)
        elif 'sealion' in llm:
            inputs = tokenizer(format_input(df, idx), return_tensors="pt").to(device)
            outputs = model.generate(inputs["input_ids"], max_new_tokens=1)
        else:
            inputs = tokenizer(format_input(df, idx), return_tensors="pt").to(device)
            outputs = model.generate(**inputs, max_new_tokens=1)
        answer_decoded = tokenizer.batch_decode(outputs, skip_special_tokens=True)

        last_element = answer_decoded[-1]
        answer = last_element.split()[-1]
        answers.append(answer)

    end = time.time()
    duration = end - start
    print('Time taken for running inference: ', duration)

    df['answer'] = answers
    logging.info(df.head())

    # save the answer csv
    df[['id','answer']].to_csv(f"./logs/{path}.csv", index = False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Your script description here")

    # Add command-line arguments
    parser.add_argument("--llm", type=str, default="bigscience/bloom-1b7",
                        help="Specify the llm value (default: bigscience/bloom-1b7)")
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu",
                        help="Specify the device")
    parser.add_argument("--folder", type=str, default="./vmlu_v1.5/",
                        help="Specify the folder data")

    # Parse the command-line arguments6
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args)
