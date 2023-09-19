VMLU is a human-centric benchmark suite specifically designed to evaluate the general capabilities of foundational models with a focus on the Vietnamese language. This benchmark covers 60 subjects spanning four categories: STEM, Humanities, Social Sciences, and more. It ranges in difficulty from an elementary level to an advanced professional level, and tests both general knowledge and problem-solving ability. Please visit our [website](https://veval.ai) for more details. 

We hope VMLU could help developers track the progress and analyze the important strengths/shortcomings of their models.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Leaderboard](#leaderboard)
    - [Zero-shot](#zero-shot)
    - [Five-shot](#five-shot)
- [Data](#data)
    - [Download](#download)
    - [JSONL format](#jsonl-format)
    - [Dataset structure](#dataset-structure)
- [How to Evaluate on VMLU](#how-to-evaluate-on-vmlu)
- [How to submit](#how-to-submit)
- [TODO](#todo)
- [Licenses](#licenses)



## Leaderboard

Below are zero-shot and five-shot accuracies from the models that we evaluate in the initial release, please visit our official.

#### Zero-shot
| Model               | STEM | Social Science | Humanities | Other | Average |
| ------------------- | :--: | :------------: | :--------: | :---: | :-----: |


#### Five-shot
| Model               | STEM | Social Science | Humanities | Other | Average |
| ------------------- | :--: | :------------: | :--------: | :---: | :-----: |


## Data

#### Download

Download the zip file: Please visit our [website](https://veval.ai):


#### JSONL format
To facilitate usage, we have organized the subject name handlers and English/Vietnamese names corresponding to 60 subjects. Questions extracted from datasets are presented in both LaTeX and non-LaTeX formats.


#### Dataset structure
VMLU dataset covers 61 subjects including 10973 multiple-choice questions and answers in Vietnamese language.

|   Id | Subject                                                 |   Number of questions |
|-----:|:--------------------------------------------------------|----------------------:|
|   01 | high_school_history                                     |                   200 |
|   02 | elementary_science                                      |                   200 |
|   03 | middle_school_history                                   |                   200 |
|   04 | elementary_mathematics                                  |                   200 |
|   05 | operating_system                                        |                   200 |
|   06 | macroeconomics                                          |                   200 |
|   07 | microeconomics                                          |                   200 |
|   08 | high_school_biology                                     |                   200 |
|   09 | criminal_law                                            |                   200 |
|   10 | middle_school_physics                                   |                   200 |
|   11 | civil_law                                               |                   197 |
|   12 | revolutionary_policy_of_the_vietnamese_commununist_part |                   200 |
|   13 | education_law                                           |                   179 |
|   14 | middle_school_literature                                |                   200 |
|   15 | introduction_to_vietnam_culture                         |                   200 |
|   16 | business_law                                            |                   200 |
|   17 | administrative_law                                      |                   193 |
|   18 | middle_school_civil_education                           |                   192 |
|   19 | preschool_pedagogy                                      |                    92 |
|   20 | economic_law                                            |                   151 |
|   21 | idealogical_and_moral_cultivation                       |                   200 |
|   22 | elementary_history                                      |                   197 |
|   23 | middle_school_geography                                 |                   185 |
|   24 | sociology                                               |                   194 |
|   25 | middle_school_biology                                   |                   185 |
|   27 | high_school_chemistry                                   |                   193 |
|   28 | high_school_physics                                     |                   187 |
|   29 | high_school_civil_education                             |                   196 |
|   30 | high_school_geography                                   |                   178 |
|   31 | high_school_literature                                  |                   194 |
|   32 | vietnamese_language_and_literature                      |                   195 |
|   33 | applied_informatics                                     |                   185 |
|   34 | history_of_world_civilization                           |                   192 |
|   35 | introduction_to_laws                                    |                   192 |
|   36 | principles_of_marxism_and_leninism                      |                   200 |
|   37 | ho_chi_minh_ideology                                    |                   194 |
|   38 | logic                                                   |                   176 |
|   39 | driving_license_certificate                             |                   191 |
|   40 | tax_civil_servant                                       |                   187 |
|   41 | civil_servant                                           |                   196 |
|   42 | introduction_to_chemistry                               |                   191 |
|   43 | introduction_to_physics                                 |                   195 |
|   44 | introduction_to_programming                             |                   200 |
|   45 | computer_architecture                                   |                   200 |
|   46 | computer_network                                        |                   195 |
|   47 | electrical_engineering                                  |                   192 |
|   48 | clinical_pharmacology                                   |                   193 |
|   49 | internal_basic_medicine                                 |                   197 |
|   50 | tax_accountant                                          |                   195 |
|   51 | accountant                                              |                   189 |
|   52 | environmental_engineering                               |                   188 |
|   53 | metrology_engineer                                      |                   194 |
|   54 | business_administration                                 |                   144 |
|   55 | labor_law                                               |                    47 |
|   56 | tax_law                                                 |                    48 |
|   57 | middle_school_chemistry                                 |                   191 |
|   58 | high_school_mathematics                                 |                   162 |
|   59 | middle_school_mathematics                               |                   109 |
|   60 | discrete_mathematics                                    |                   151 |
|   61 | statistics_and_probability                              |                   171 |


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



## How to Evaluate on VMLU
You can evaluate model on the validation set of VMLU through [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness), which is a framework for few-shot evaluation of autoregressive language models.  
```bash

python main.py --model hf-causal --model_args pretrained=EleutherAI/gpt-j-6B --tasks vmlu --device cuda:0
```

Please refer to [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) for more details.

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

Then you can submit the prepared csv file [here](https://veval.ai), **note that you need to first log in to access the submission page**.


## TODO
TBU


## Licenses
TBU
