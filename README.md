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


# <div align="center"><b>From-Scratch Models Leaderboard</b></div>

#### Zero-shot
| #  | Model                           |  Organization  | Base Model |  Accessibility  | Evaluation Date | STEM  | Social Science  | Humanities | Other  | Average |
| -- | -------------------             |  :---------:   | :--------: |  :-----------:  | :-----------:   | :--:  | :------------:  | :--------: | :---:  | :-----: |
| 1  | GPT-4                     |  OpenAI                                    | From scratch   |  API     | 08/01/2024 |  63.84 |            71.78 |      66.14 |   60.37 |   65.53 |
| 2  | ChatGPT                   |  OpenAI                                    | From scratch   |  API     | 08/01/2024 |  43.24 |            51.67 |      46.96 |   46.32 |   46.33 |
| 3  | ViGPT-1.6B-v1             |  Vin BigData                               | From scratch   |  Private | 08/01/2024 |  35.06 |            48.72 |      47.20 |   42.54 |   42.34 |
| 4  | Qwen-7B                   |  Alibaba Cloud                             | From scratch   |  Weight  | 08/01/2024 |  30.64 |            35.07 |      34.15 |   32.68 |   32.81 |
| 5  | sealion7b                 |  AI Singapore                              | From scratch   |  Weight  | 08/01/2024 |  26.28 |            28.57 |      27.66 |   27.34 |   26.73 |
| 6  | bloom-1b7                 |  BigScience                                | From scratch   |  Weight  | 08/01/2024 |  25.13 |            25.09 |      26.34 |   25.19 |   25.51 |
| 7  | bloom-7b1                 |  BigScience                                | From scratch   |  Weight  | 08/01/2024 |  25.08 |            26.26 |      25.74 |   24.59 |   25.41 |
| 8  | falcon-7b                 |  Technology Innovation Institute           | From scratch   |  Weight  | 08/01/2024 |  24.19 |            23.59 |      26.72 |   24.73 |   24.96 |
| 9  | PhoGPT-7B5-Instruct       |  Vin AI                                    | From scratch   |  Weight  | 08/01/2024 |  21.97 |            25.93 |      24.32 |   26.00 |   24.01 |
| 10 | Llama-2-7b-hf             |  Facebook Research - Meta                  | From scratch   |  Weight  | 08/01/2024 |  21.48 |            23.41 |      24.10 |   23.59 |   22.95 |
| 11 | falcon-7b-instruct        |  Technology Innovation Institute           | From scratch   |  Weight  | 08/01/2024 |  9.50  |            13.63 |      14.98 |   6.13  |   11.39 |  
# <div align="center"><b>Finetuned Models Leaderboard</b></div>

| #  | Model                           |  Organization  | Base Model |  Accessibility  | Evaluation Date | STEM  | Social Science  | Humanities | Other  | Average |
| -- | -------------------             |  :---------:   | :--------: |  :-----------:  | :-----------:   | :--:  | :------------:  | :--------: | :---:  | :-----: |
| 1  | Vistral-7B-Chat           |  UONLP x Ontocord                          | Mistral-7B-v0.1|  Weight  | 15/01/2024 |  43.43 |            57.02 |      55.12 |   48.01 |   50.07 |
| 2  | bloomz-7b1                |  BigScience                                | bloom-7b1      |  Weight  | 08/01/2024 |  32.63 |            45.73 |      41.85 |   39.89 |   38.87 |
| 3  | vbd-llama2-7b-50b-chat    |  Vin BigData                               | llama-2-7b     |  Weight  | 08/01/2024 |  31.45 |            40.34 |      40.24 |   39.62 |   36.98 |
| 4  | vietcuna-3b               |  Virtual Interactive                       | bloomz-3b      |  Weight  | 08/01/2024 |  30.12 |            39.92 |      37.86 |   33.83 |   34.79 |
| 5  | bloomz-1b7                |  BigScience                                | bloom-1b7      |  Weight  | 08/01/2024 |  29.72 |            40.17 |      34.73 |   33.41 |   33.65 |
| 6  | SeaLLM-7B-Hybrid          |  DAMO Academy                              | llama-2-7b     |  Weight  | 08/01/2024 |  29.49 |            34.61 |      36.68 |   34.52 |   33.39 |
| 7  | ura-llama-7b              |  Ho Chi Minh City University of Technology | llama-2-7b     |  Weight  | 08/01/2024 |  29.19 |            33.31 |      34.64 |   32.97 |   32.18 |
| 8  | vinallama-7b-chat         |  Virtual Interactive                       | llama-2-7b     |  Weight  | 08/01/2024 |  25.70 |            34.50 |      33.87 |   31.41 |   30.64 |
| 9  | vietcuna-7b-v3            |  Virtual Interactive                       | bloomz-7b      |  Weight  | 08/01/2024 |  28.70 |            33.94 |      31.32 |   28.24 |   30.34 |
| 10 | vietnamese-llama-7b-40GB  |  BKAI - HUST                               | llama-2-7b     |  Weight  | 08/01/2024 |  23.22 |            25.61 |      26.71 |   26.30 |   25.19 |

#### Few-shot
| Model               | STEM | Social Science | Humanities | Other | Average |
| ------------------- | :--: | :------------: | :--------: | :---: | :-----: |
| GPT-4               | TBU  |      TBU       |    TBU     | TBU   |  TBU    |




## How to Evaluate on VMLU
You can just follow our code
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
