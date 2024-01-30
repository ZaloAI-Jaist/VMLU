import os
import openai
import json
import tqdm
import pandas as pd
import time
import re
openai.api_key = os.environ['GPT_KEY']


if __name__ == "__main__":
    data = []
    with open('vmlu_v2/test.jsonl', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(json.loads(line))

    # data = data[:1] # for debuging only
    all_res = []
    for idx, doc in enumerate(tqdm.tqdm(data[:])):
        text_choice = '\n'.join(doc['choices'])
        prompt = "Chỉ đưa ra chữ cái đứng trước câu trả lời đúng (A, B, C, D hoặc E) của câu hỏi trắc nghiệm sau: \n" \
                + doc["question"] \
                + "\n\n" \
                + text_choice \
                + "\n" \
                + "Đáp án: " 
        
        messages = [{"role": "user", "content": prompt}]
        response=None
        timeout_counter=0
        while response is None and timeout_counter<=30:
            try:
                response = openai.ChatCompletion.create(
                    model='gpt-3.5-turbo',
                    messages=messages,
                    temperature=0,
                )
            except Exception as msg:
                print(msg)
                print('sleeping because of exception ...')
                time.sleep(30)
                continue
                
        if response==None:
            response_str=""
        else:
            response_str = response['choices'][0]['message']['content']
    
        
        all_res.append({
            "id": doc['id'],
            "prompt": prompt,
            "question": doc["question"],
            "answer": response_str
        })

        result_folder = "all_res/gpt_result"
        os.makedirs(result_folder, exist_ok=True)
        
        if idx % 100 == 0:
            pd.DataFrame(all_res).to_csv(f"all_res/gpt_result/raw_result_{len(all_res)}.csv", index=False)
    
    df = pd.DataFrame(all_res)
    df['answer'] = df.answer.map(lambda x: x[0].lower())
    df['answer'] = df['answer'].map(lambda x: re.sub(r'[^abcde]', '', x))
    submission_csv = df[['id', 'answer']].to_csv('submission.csv', index=None)
