import pandas as pd
import numpy as np
import torch
import json
import glob
import logging  
import os
import argparse

from transformers import AutoModelForCausalLM, BitsAndBytesConfig, AutoTokenizer
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

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )
    max_memory = {0: "23GiB", "cpu": "80GiB"}

    model = AutoModelForCausalLM.from_pretrained(llm,
                                                quantization_config=bnb_config,
                                                device_map={'':device},
                                                trust_remote_code=True,
                                                use_auth_token=False,
                                                max_memory=max_memory)
    model.config.use_cache = False
    tokenizer = AutoTokenizer.from_pretrained(llm)

    # Create empty lists to store data
    ids = []
    questions = []
    choices_A = []
    choices_B = []
    choices_C = []
    choices_D = []
    choices_E = []
    gold = []
    # Read JSONL files
    data_path = Path(folder)
    jsonl_files = data_path.glob("*.jsonl")

    for file in jsonl_files:
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                data = json.loads(line)
                ids.append(data["id"])
                questions.append(data["question"])
                choices = data["choices"]
                gold.append(data["answer"])
                try:
                    choices_A.append(choices[0])
                except:
                    choices_A.append(None)
                try:
                    choices_B.append(choices[1])
                except:
                    choices_B.append(None)
                try:
                    choices_C.append(choices[2])
                except:
                    choices_C.append(None)
                try:
                    choices_D.append(choices[3])
                except:
                    choices_D.append(None)
                try:
                    choices_E.append(choices[4])
                except:
                    choices_E.append(None)

    # Create a DataFrame
    df = pd.DataFrame({
        "id": ids,
        "prompt": questions,
        "A": choices_A,
        "B": choices_B,
        "C": choices_C,
        "D": choices_D,
        "E": choices_E,
        "gold": gold
    })
    logging.info(df.head())

    preamble = \
        'Trả lời câu hỏi sau bằng cách đưa ra chữ cái của câu trả lời đúng: '

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
        outputs = model.generate(**inputs, max_new_tokens=1, pad_token_id=tokenizer.eos_token_id)
    else:
        inputs = tokenizer(format_input(df, 0), return_tensors="pt").to(device)
        outputs = model.generate(**inputs, max_new_tokens=1)

    answer = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    logging.info('Contruct a toy eg')
    logging.info("Generated answer: %s", answer)

    correct = 0
    answers = []

    for idx in tqdm(df.index):
        if 'falcon' in llm:
            inputs = tokenizer(format_input(df, idx), return_tensors="pt", return_token_type_ids=False).to(device)
            outputs = model.generate(**inputs, max_new_tokens=1, pad_token_id=tokenizer.eos_token_id)
        elif 'llama' in llm:
            inputs = tokenizer(format_input(df, idx), return_tensors="pt").to(device)
            outputs = model.generate(**inputs, max_new_tokens=1)
        else:
            inputs = tokenizer(format_input(df, idx), return_tensors="pt").to(device)
            outputs = model.generate(**inputs)
        answer = tokenizer.batch_decode(outputs, skip_special_tokens=True)

        last_element = answer[-1]
        answer = last_element.split()[-1]
        answers.append(answer)

        if answer.strip() == df.loc[idx, 'gold'].strip():
            correct += 1

    df['answer'] = answers
    logging.info(df.head())

    # save the answer csv
    df[['id','answer']].to_csv(f"./logs/{path}.csv", index = False)

    accuracy = correct / len(df)
    logging.info("Accuracy: %.2f%%", accuracy * 100)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Your script description here")

    # Add command-line arguments
    parser.add_argument("--llm", type=str, default="bigscience/bloom-1b7",
                        help="Specify the llm value (default: bigscience/bloom-1b7)")
    parser.add_argument("--device", type=str, default="cuda:6" if torch.cuda.is_available() else "cpu",
                        help="Specify the device (default: 'cuda:2')")
    parser.add_argument("--folder", type=str, default="code_benchmark/vmlu_v2" if torch.cuda.is_available() else "cpu",
                        help="Specify the folder data")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args)
