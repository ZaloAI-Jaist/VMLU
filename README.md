VMLU is a human-centric benchmark suite specifically designed to evaluate the general capabilities of foundational models with a focus on the Vietnamese language. This benchmark covers 58 subjects spanning four categories: STEM, Humanities, Social Sciences, and more. It ranges in difficulty from an elementary level to an advanced professional level, and tests both general knowledge and problem-solving ability. Please visit our [website](https://vmlu.ai) for more details. 

We hope VMLU could help developers track the progress and analyze the important strengths/shortcomings of their models.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Data](#data)
    - [Download](#download)
    - [JSONL format](#jsonl-format)
    - [Dataset structure](#dataset-structure)
- [Leaderboard](#leaderboard)
    - [Zero-shot](#zero-shot)
    - [Few-shot](#few-shot)
- [How to Evaluate on VMLU](#how-to-evaluate-on-vmlu)
- [How to submit](#how-to-submit)
- [TODO](#todo)
- [Licenses](#licenses)



## Data

#### Download

Download the zip file: Please visit our [website](https://vmlu.ai/#DataSection):


#### JSONL format
To facilitate usage, we have organized the subject name handlers and English/Vietnamese names corresponding to 58 subjects. Questions extracted from datasets are presented in both LaTeX and non-LaTeX formats.


#### Dataset structure
VMLU dataset covers 58 subjects including 10,880 multiple-choice questions and answers in Vietnamese language.

|   Id | Subject                                                 | Category       |   Number of questions |
|-----:|:--------------------------------------------------------|:---------------|----------------------:|
|   01 | Elementary Mathematics                                  | STEM           |                   200 |
|   02 | Elementary Science                                      | STEM           |                   200 |
|   03 | Middle School Biology                                   | STEM           |                   188 |
|   04 | Middle School Chemistry                                 | STEM           |                   200 |
|   05 | Middle School Mathematics                               | STEM           |                   119 |
|   06 | Middle School Physics                                   | STEM           |                   200 |
|   07 | High School Biology                                     | STEM           |                   200 |
|   08 | High School Chemistry                                   | STEM           |                   200 |
|   09 | High School Mathematics                                 | STEM           |                   163 |
|   10 | High School Physics                                     | STEM           |                   200 |
|   11 | Applied Informatics                                     | STEM           |                   200 |
|   12 | Computer Architecture                                   | STEM           |                   200 |
|   13 | Computer Network                                        | STEM           |                   197 |
|   14 | Discrete Mathematics                                    | STEM           |                   182 |
|   15 | Electrical Engineering                                  | STEM           |                   194 |
|   16 | Introduction to Chemistry                               | STEM           |                   197 |
|   17 | Introduction to Physics                                 | STEM           |                   191 |
|   18 | Introduction to Programming                             | STEM           |                   197 |
|   19 | Metrology Engineer                                      | STEM           |                   155 |
|   20 | Operating System                                        | STEM           |                   200 |
|   21 | Statistics and Probability                              | STEM           |                   192 |
|   22 | Middle School Civil Education                           | Social Science |                   196 |
|   23 | Middle School Geography                                 | Social Science |                   162 |
|   24 | High School Civil Education                             | Social Science |                   200 |
|   25 | High School Geography                                   | Social Science |                   179 |
|   26 | Business Administration                                 | Social Science |                   192 |
|   27 | Ho Chi Minh Ideology                                    | Social Science |                   197 |
|   28 | Macroeconomics                                          | Social Science |                   200 |
|   29 | Microeconomics                                          | Social Science |                   200 |
|   30 | Principles of Marxism and Leninism                      | Social Science |                   200 |
|   31 | Sociology                                               | Social Science |                   196 |
|   32 | Elementary History                                      | Humanity       |                   195 |
|   33 | Middle School History                                   | Humanity       |                   200 |
|   34 | Middle School Literature                                | Humanity       |                   192 |
|   35 | High School History                                     | Humanity       |                   200 |
|   36 | High School Literature                                  | Humanity       |                   200 |
|   37 | Administrative Law                                      | Humanity       |                   100 |
|   38 | Business Law                                            | Humanity       |                   197 |
|   39 | Civil Law                                               | Humanity       |                   200 |
|   40 | Criminal Law                                            | Humanity       |                   180 |
|   41 | Economic Law                                            | Humanity       |                   178 |
|   42 | Education Law                                           | Humanity       |                   183 |
|   43 | History of World Civilization                           | Humanity       |                   200 |
|   44 | Idealogical and Moral Cultivation                       | Humanity       |                   200 |
|   45 | Introduction to Laws                                    | Humanity       |                   139 |
|   46 | Introduction to Vietnam Culture                         | Humanity       |                   200 |
|   47 | Logic                                                   | Humanity       |                   192 |
|   48 | Revolutionary Policy of the Vietnamese Commununist Part | Humanity       |                   200 |
|   49 | Vietnamese Language and Literature                      | Humanity       |                   192 |
|   50 | Accountant                                              | Other          |                   186 |
|   51 | Clinical Pharmacology                                   | Other          |                   200 |
|   52 | Environmental Engineering                               | Other          |                   189 |
|   53 | Internal Basic Medicine                                 | Other          |                   189 |
|   54 | Preschool Pedagogy                                      | Other          |                   112 |
|   55 | Tax Accountant                                          | Other          |                   192 |
|   56 | Tax Civil Servant                                       | Other          |                   189 |
|   57 | Civil Servant                                           | Other          |                   189 |
|   58 | Driving License Certificate                             | Other          |                   189 |


Below is a non-LaTeX example from dev.jsonl:

  ```
  {
    "id": "51-0001",
    "question": "Các phát biểu ĐÚNG về ĐỊNH NGHĨA Dược lâm sàng, NGOẠI TRỪ:",
    "choices": [
      'A. Là ngành khoa học về sử dụng thuốc hợp lý',
      'B. Nghiên cứu phát triển kinh tế dược bệnh viện',
      'C. Giúp tối ưu hóa việc sử dụng thuốc trên cơ sở về dược và y sinh học',
      'D. Đối tượng chính của môn học dược lâm sàng là thuốc và người bệnh'
    ],
    "answer": "B"
  }
  ```


Below is a LaTeX example from dev.jsonl:
  ```
  {
    "id": "58-0006",
    "question": "Trong không gian Oxyz, cho đường thẳng d:{\\frac{x-2}{1}}=\\frac{y-1}{-2}=\\frac{z+1}{3}. Điểm nào dưới đây thuộc d ?",
    "choices": [
      "A. Q\\left(2;{1};{1}\\right)",
      "B. M\\left(1;{2};{3}\\right)",
      "C. N\\left(1;{-}2;{3}\\right)",
      "D. P\\left(2;{1};{-}1\\right)"
    ],
    "answer": "D"
  }
  ```




## Leaderboard

Below are zero-shot and five-shot accuracies from the models that we evaluate in the initial release, please visit our official website.

<span style="color:red">DISCLAIMER: Please note that evaluating models like LLMs can be challenging, as leaderboards might be susceptible to manipulation, and a small tweak in prompting can lead to totally different results. It's especially concerning because some models are not publicly accessible. For instance, good results can be achieved through distilling answers from stronger models like GPT-4 or even from humans. Therefore, it's important to approach leaderboard scores with caution. Most of the  models assessed here are public With Open Access, which have public weights or APIs for verification.</span>


#### Zero-shot
| Model                               | STEM  | Social Science  | Humanities | Other  | Average |
| -------------------                 | :--:  | :------------:  | :--------: | :---:  | :-----: |
| GPT-4          |  63.84 |            71.78 |      66.14 |   60.37 |   65.53 |
| ChatGPT        |  41.63 |            54.25 |      50.3  |   47.97 |   48.54 |
| KiLM-3B-V1     |  34.58 |            48.53 |      47.65 |   42.75 |   42.31 |
| bloomz-7b1     |  31.99 |            44.92 |      40.43 |   39.71 |   38.04 |
| vietcuna-3b    |  30.18 |            39.12 |      37.11 |   32.79 |   34.28 |
| bloomz-1b7     |  28.99 |            38.78 |      34.18 |   35.09 |   33.24 |
| ura-llama-7b   |  27.48 |            28.66 |      30.79 |   29.03 |   28.95 |
| vietcuna-7b-v3 |  26.21 |            31.16 |      29.96 |   26.81 |   28.32 |
| Llama-2-7b     |  26.75 |            27.57 |      28.67 |   28.79 |   27.81 |
| bloom-7b1      |  25.66 |            26.84 |      25.71 |   23.47 |   25.54 |
| bloom-1b7      |  25.53 |            25.45 |      25.95 |   24.86 |   25.54 |
| falcon-7b      |  24.30 |            24.04 |      26.10 |   23.53 |   24.70 |

#### Few-shot
| Model               | STEM | Social Science | Humanities | Other | Average |
| ------------------- | :--: | :------------: | :--------: | :---: | :-----: |
| GPT-4               | TBU  |      TBU       |    TBU     | TBU   |  TBU    |




## How to Evaluate on VMLU
You can evaluate model on the validation set of VMLU through [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness), which is a framework for few-shot evaluation of autoregressive language models.

```bash

python main.py --model hf-causal --model_args pretrained=EleutherAI/gpt-j-6B --tasks vmlu --device cuda:0
```
Please refer to [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) for more details.


Or you can just follow our code
```bash
cd code_benchmark;
GPTKEY='<YOUR GPT KEY>' python test_gpt.py
```


## How to submit
You need to first prepare a UTF-8 encoded CSV file with the following format, please refer to submission_example.csv for details.

```
## key within each subject is the "id" field from the dataset
id,answer
41-0001,A
41-0002,A
41-0003,A
41-0004,C
41-0005,A
```

Then you can submit the prepared csv file [here](https://vmlu.ai/submit), **note that you need to first log in to access the submission page**.


## TODO
TBU


## Licenses
TBU
