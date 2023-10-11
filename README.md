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
VMLU dataset covers 58 subjects including 10933 multiple-choice questions and answers in Vietnamese language.

|   Id | Subject                                                 |   Number of questions |
|-----:|:--------------------------------------------------------|----------------------:|
|   01 | high_school_history                                     |                   200 |
|   02 | elementary_science                                      |                   200 |
|   03 | middle_school_history                                   |                   200 |
|   04 | elementary_mathematics                                  |                   200 |
|   05 | operating_system                                        |                   199 |
|   06 | macroeconomics                                          |                   200 |
|   07 | microeconomics                                          |                   200 |
|   08 | high_school_biology                                     |                   200 |
|   09 | criminal_law                                            |                   197 |
|   10 | middle_school_physics                                   |                   200 |
|   11 | civil_law                                               |                   200 |
|   12 | revolutionary_policy_of_the_vietnamese_commununist_part |                   200 |
|   13 | education_law                                           |                   186 |
|   14 | middle_school_literature                                |                   192 |
|   15 | introduction_to_vietnam_culture                         |                   200 |
|   16 | business_law                                            |                   200 |
|   17 | administrative_law                                      |                   109 |
|   18 | middle_school_civil_education                           |                   196 |
|   19 | preschool_pedagogy                                      |                   112 |
|   20 | economic_law                                            |                   191 |
|   21 | idealogical_and_moral_cultivation                       |                   200 |
|   22 | elementary_history                                      |                   195 |
|   23 | middle_school_geography                                 |                   162 |
|   24 | sociology                                               |                   196 |
|   25 | middle_school_biology                                   |                   188 |
|   26 | middle_school_chemistry                                 |                   200 |
|   27 | high_school_chemistry                                   |                   200 |
|   28 | high_school_physics                                     |                   200 |
|   29 | high_school_civil_education                             |                   199 |
|   30 | high_school_geography                                   |                   179 |
|   31 | high_school_literature                                  |                   200 |
|   32 | vietnamese_language_and_literature                      |                   192 |
|   33 | applied_informatics                                     |                   200 |
|   34 | history_of_world_civilization                           |                   200 |
|   35 | introduction_to_laws                                    |                   152 |
|   36 | principles_of_marxism_and_leninism                      |                   200 |
|   37 | ho_chi_minh_ideology                                    |                   197 |
|   38 | logic                                                   |                   192 |
|   39 | driving_license_certificate                             |                   189 |
|   40 | tax_civil_servant                                       |                   189 |
|   41 | civil_servant                                           |                   189 |
|   42 | introduction_to_chemistry                               |                   197 |
|   43 | introduction_to_physics                                 |                   191 |
|   44 | introduction_to_programming                             |                   197 |
|   45 | computer_architecture                                   |                   200 |
|   46 | computer_network                                        |                   197 |
|   47 | electrical_engineering                                  |                   194 |
|   48 | clinical_pharmacology                                   |                   200 |
|   49 | internal_basic_medicine                                 |                   189 |
|   50 | tax_accountant                                          |                   192 |
|   51 | accountant                                              |                   186 |
|   52 | environmental_engineering                               |                   189 |
|   53 | metrology_engineer                                      |                   155 |
|   54 | business_administration                                 |                   189 |
|   58 | high_school_mathematics                                 |                   163 |
|   59 | middle_school_mathematics                               |                   119 |
|   60 | discrete_mathematics                                    |                   182 |
|   61 | statistics_and_probability                              |                   192 |


Below is a non-LaTeX example from dev.jsonl:

  ```
  {
    "id": "51-0001",
    "question": "Những trường hợp nào sau đây được xác định là nghiệp vụ kinh tế phát sinh và ghi vào sổ kế toán.",
    "choices": [
      "A. Ký hợp đồng thuê nhà xưởng để sản xuất, giá trị hợp đồng 20 triệu đồng/năm",
      "B. Mua TSCĐ 50 triệu chưa thanh toán",
      "C. Nhận được lệnh chi tiền phục vụ tiếp khách của doanh nghiệp 5 triệu",
      "D. Tất cả các trường hợp trên"
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

#### Zero-shot
| Model                               | STEM  | Social Science  | Humanities | Other  | Average |
| -------------------                 | :--:  | :------------:  | :--------: | :---:  | :-----: |
| GPT-4          |  63.84 |            71.78 |      66.14 |   60.37 |   65.53 |
| ChatGPT        |  41.63 |            54.25 |      50.3  |   47.97 |   48.54 |
| KiLM-3B-V1     |  34.58 |            48.53 |      47.65 |   42.75 |   42.31 |
| bloomz-7b1     |  33.28 |            47.35 |      42.64 |   40.51 |   39.73 |
| vietcuna-3b    |  31.89 |            42.37 |      39.88 |   36.59 |   36.71 |
| bloomz-1b7     |  29.46 |            39.17 |      35.35 |   34.04 |   33.67 |
| vietcuna-7b-v3 |  30.98 |            37.41 |      34.51 |   31.41 |   33.25 |
| bloom-7b       |  27.32 |            27.99 |      25.47 |   25.87 |   26.64 |
| bloom-1b7      |  25.68 |            24.45 |      25.55 |   24.89 |   25.31 |
| Llama-2-7b     |   0.24 |             0.57 |       0.45 |    0.39 |    0.39 |
| falcon-7b      |   0.11 |             0.11 |       0    |    0.13 |    0.08 |

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
id, answer
41-0001, A
41-0002, A
41-0003, A
41-0004, C
41-0005, A
```

Then you can submit the prepared csv file [here](https://vmlu.ai/submit), **note that you need to first log in to access the submission page**.


## TODO
TBU


## Licenses
TBU
