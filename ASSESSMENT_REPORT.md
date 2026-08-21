# Hindi → English Idiom Translation Model
## Final AI/ML Assessment Report

---

## 1. Project Title

**Hindi → English Idiom Translation using MarianMT Fine-Tuning**

---

## 2. Project Overview

This project develops a Hindi → English neural machine translation system
specialized in translating Hindi idiomatic expressions into meaningful English.

The project started with a general Hindi → English translation model and
progressively improved it through dataset preparation, general fine-tuning,
idiom identification, idiom verification, idiom-specific dataset creation,
idiom-specific fine-tuning, evaluation, and API development.

The final system uses a fine-tuned MarianMT model based on the
`Helsinki-NLP/opus-mt-hi-en` architecture.

The project demonstrates an end-to-end AI/ML workflow:

Hindi sentence
        ↓
Dataset preparation
        ↓
General Hindi → English fine-tuning
        ↓
Hindi idiom identification
        ↓
Idiom verification
        ↓
Idiom-specific training dataset
        ↓
Idiom-specific fine-tuning
        ↓
Model evaluation
        ↓
FastAPI REST API
        ↓
Hugging Face Model Repository

---

## 3. Problem Statement

General machine translation models may translate idioms literally instead of
preserving their intended meaning.

For example, a Hindi idiom may contain words whose literal English translation
does not represent the actual meaning of the expression.

Therefore, the objective of this project is to adapt a Hindi → English
translation model so that it can better handle Hindi idiomatic expressions
within contextual sentences.

---

## 4. Objectives

The main objectives of the project are:

- Build a Hindi → English translation pipeline.
- Use a pretrained neural machine translation model.
- Fine-tune the model using Hindi-English parallel data.
- Identify Hindi idiomatic expressions.
- Create and verify an idiom-focused dataset.
- Fine-tune the model specifically for Hindi idiom translation.
- Evaluate the model using BLEU and METEOR.
- Compare performance before and after idiom-specific fine-tuning.
- Test the model on unseen idiomatic sentences.
- Expose the trained model through a REST API.
- Publish the trained model on Hugging Face.
- Maintain the project using Git and GitHub.

---

## 5. Technologies Used

- Python 3.11
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- MarianMT
- Pandas
- NumPy
- SacreBLEU
- NLTK
- SentencePiece
- Sacremoses
- FastAPI
- Uvicorn
- Git
- GitHub
- Hugging Face Hub
- Render

---

## 6. Pretrained Model

The project uses:

`Helsinki-NLP/opus-mt-hi-en`

This is a pretrained MarianMT model designed for Hindi → English
translation.

Instead of training a translation model from scratch, the existing pretrained
model was adapted using task-specific Hindi-English data.

---

## 7. Dataset

The general translation dataset was obtained from the IITB Hindi-English
parallel dataset available through Hugging Face:

`cfilt/iitb-english-hindi`

The dataset contains Hindi-English parallel sentence pairs.

Initial dataset inspection was performed before training to understand the
available fields and translation structure.

---

## 8. General Dataset Preparation

The project initially inspected a sample of the dataset and created a clean
Hindi-English translation dataset.

The general dataset preparation included:

- Loading the dataset.
- Inspecting Hindi and English fields.
- Removing invalid or missing translation pairs.
- Creating training data.
- Creating validation data.
- Saving the processed datasets as CSV files.

Final valid general dataset:

| Dataset | Examples |
|---|---:|
| Training | 47,985 |
| Validation | 1,999 |
| Total | 49,984 |

---

## 9. General Hindi → English Fine-Tuning

The pretrained MarianMT model was fine-tuned using the prepared
Hindi-English parallel dataset.

The model learned from Hindi input sentences and corresponding English target
translations.

The trained model was saved locally for further evaluation.

The project also created a larger training configuration and evaluated the
general translation performance before moving to idiom specialization.

---

## 10. Idiom-Specific Translation Problem

General translation performance does not necessarily mean that the model
understands idiomatic meaning.

For example:

Hindi:

`अपना उल्लू सीधा करना`

The literal words refer to "making one's owl straight", but the intended
meaning is to serve one's own interests.

Therefore, a separate idiom-focused dataset was created to improve the model's
ability to translate idioms according to their intended meaning.

---

## 11. Idiom Extraction

The project created an idiom identification pipeline.

The workflow included:

1. Extracting potential idiomatic expressions.
2. Filtering candidate expressions.
3. Reviewing candidate idioms.
4. Verifying idiom candidates.
5. Creating contextual Hindi sentences.
6. Providing appropriate English translations.
7. Preparing the final idiom training dataset.

This produced a verified collection of Hindi idiomatic examples.

---

## 12. Idiom Dataset

The verified idiom data contains contextual Hindi sentences together with their
English translations and idiom information.

The final idiom-specific training dataset contained:

**63 training examples**

The examples covered a variety of Hindi idiomatic expressions, including:

- हाथ जोड़ना
- मुँहतोड़ जवाब
- अपना उल्लू सीधा करना
- पल्ले नहीं पड़ना
- आस्तीन का सांप
- बाल-बाल बचना
- मीन-मेख निकालना
- जले पर नमक छिड़कना
- नाक कटना
- मक्खीचूस
- दाल में कुछ काला होना
- घोड़े बेचकर सोना
- हाँ में हाँ मिलाना

and other idiomatic expressions.

---

## 13. Idiom-Specific Fine-Tuning

The verified idiom dataset was used to fine-tune the pretrained translation
model further.

The final model was saved as:

`fine_tuned_idiom_model`

The model contains the trained MarianMT weights and tokenizer files required
for inference.

The idiom-specific fine-tuning process was completed successfully.

---

## 14. Final Idiom Model

Final model directory:

```text
fine_tuned_idiom_model/
```
The trained model contains files such as:

config.json
generation_config.json
model.safetensors
source.spm
target.spm
tokenizer_config.json
training_args.bin
vocab.json

The trained model was also uploaded to Hugging Face.

Hugging Face repository:

NivethaT/hindi-english-idiom-translation

---

# 15. Model Evaluation

The final idiom-specialized model was evaluated using:

BLEU
METEOR
Average Word Overlap
Exact Match
Unseen Idiom Evaluation

---

# 16. BLEU Evaluation

BLEU was used to measure similarity between the model-generated English
translation and the reference English translation.

The final idiom-specific evaluation contained:

63 examples

Final idiom model:

BLEU = 14.16

or approximately:

14.16%

---

# 17. METEOR Evaluation

METEOR was additionally used as an evaluation metric.

The final idiom-specialized model achieved:

METEOR = 0.324295

or:

32.43%

METEOR evaluation was performed on all 63 idiom examples.

The detailed results were saved to:

data/final_idiom_meteor.csv

---

# 18. Pre-Fine-Tuning vs Post-Fine-Tuning Comparison

The idiom-specific model was compared against the earlier model.

*Final Comparison*

| Metric               | Before Idiom Fine-Tuning | After Idiom Fine-Tuning |                  Change |
| -------------------- | -----------------------: | ----------------------: | ----------------------: |
| BLEU                 |                     7.85 |                   14.16 |                   +6.31 |
| Average Word Overlap |                   37.59% |                  42.46% | +4.87 percentage points |
| Exact Matches        |                        0 |                       1 |                      +1 |


The direct comparison shows improvement in BLEU, average word overlap, and exact matches after idiom-specific fine-tuning.

The comparison data was saved to:

data/final_model_comparison.csv

METEOR was calculated for the final model as an additional evaluation metric.
A pre-fine-tuning METEOR value was not calculated, so no unsupported baseline value is reported.

---

# 19. Unseen Idiom Evaluation

To test whether the model could handle idioms that were not part of the
training examples, a separate unseen idiom test was performed.

Results:

| Metric               | Result |
| -------------------- | -----: |
| Test examples        |     15 |
| Exact matches        |      0 |
| Average Word Overlap | 45.45% |
| BLEU                 |  16.34 |

The unseen evaluation was completed successfully.

The results were saved to:

data/unseen_idiom_predictions.csv

The unseen test demonstrates that the model was evaluated on examples separate from the 63 idiom training examples.

---

# 20. Sample Final Predictions
Example 1 — Successful

Hindi:

शिक्षक ने कई बार समझाया, लेकिन बात उसके पल्ले नहीं पड़ी।

Expected:

The teacher explained it several times, but he could not understand it.

Model:

The teacher explained several times, but he could not understand.

This is a strong semantic translation.

Example 2 — Successful

Hindi:

हर काम में मीन-मेख निकालने के बजाय समाधान पर ध्यान दो।

Expected:

Instead of finding fault with everything, focus on the solution.

Model:

Instead of finding fault with everything, focus on the solution.

This is an exact match.

Example 3 — Needs Improvement

Hindi:

उसने मुँहतोड़ जवाब देकर अपने आलोचकों को चुप करा दिया।

Expected:

He gave his critics a fitting reply and silenced them.

Model:

He answered yes to his critics.

This example shows that the model still has difficulty correctly translating some idioms.

Example 4 — Needs Improvement

Hindi:

बेटे की करतूत से पूरे परिवार की नाक कट गई।

Expected:

The son's actions brought shame to the entire family.

Model:

The son 's actions cut the whole family off.

The model captures some sentence structure but interprets the idiom too literally.

---

# 21. Error Analysis

The final analysis of the 63 idiom examples showed:

| Category             | Examples |
| -------------------- | -------: |
| High Word Overlap    |       17 |
| Partial Word Overlap |       27 |
| Low Word Overlap     |       19 |
| Exact Matches        |        1 |

Average word overlap:

**42.46%**

The results indicate that the model has learned useful parts of many idiomatic sentences, but some idioms are still translated literally.

The main remaining challenges include:

Literal translation of idiomatic expressions.
Limited idiom training examples.
Differences between reference translations and generated translations.
Difficulty with rare or culturally specific idioms.
Incorrect handling of some named entities or contextual words.
Limited generalization from only 63 idiom training examples.

---

# 22. FastAPI REST API

A REST API was created using FastAPI.

The API loads the final idiom-specialized MarianMT model and provides Hindi → English translation through an HTTP endpoint.

Root Endpoint

GET /

Health Endpoint

GET /health

Translation Endpoint

POST /translate

The translation endpoint accepts:

{
  "text": "शिक्षक ने कई बार समझाया, लेकिन बात उसके पल्ले नहीं पड़ी।"
}

and returns:

{
  "source_language": "Hindi",
  "target_language": "English",
  "input": "शिक्षक ने कई बार समझाया, लेकिन बात उसके पल्ले नहीं पड़ी।",
  "translation": "The teacher explained several times, but he could not understand."
}

---

# 23. API Testing

The API was successfully tested locally using FastAPI and Uvicorn.

The following endpoints were successfully accessed:

GET /
GET /docs
GET /openapi.json
GET /health
POST /translate

The FastAPI Swagger documentation was also tested through:

http://127.0.0.1:8000/docs

The /translate endpoint successfully returned HTTP 200 responses during local testing

---

# 24. Hugging Face Model

The final trained model was uploaded to Hugging Face.

Repository:

NivethaT/hindi-english-idiom-translation

The repository contains the trained model files required for loading the
fine-tuned MarianMT model.

---

# 25. GitHub Repository

The complete source code and project documentation were maintained using Git and GitHub.

The project repository is:

https://github.com/Nivetha0508-tech/Hindi-English-Idiom-Translation

The repository includes:

api/
data/
src/
README.md
requirements.txt
.gitignore

Large model files were intentionally excluded from the Git repository and published separately through Hugging Face.

---

# 26. Project Structure

Hindi-English-Idiom-Translation/
│
├── api/
│   └── main.py
│
├── data/
│   ├── hindi_english.csv
│   ├── hindi_english_idioms.csv
│   ├── hindi_idiom_candidates.csv
│   ├── idiom_review.csv
│   ├── idiom_training.csv
│   ├── idiom_verified_candidates.csv
│   ├── verified_hindi_english_idioms.csv
│   ├── final_idiom_predictions.csv
│   ├── final_idiom_analysis.csv
│   ├── final_idiom_meteor.csv
│   ├── final_model_comparison.csv
│   └── unseen_idiom_predictions.csv
│
├── src/
│   ├── check_dataset.py
│   ├── prepare_dataset.py
│   ├── fine_tune.py
│   ├── fine_tune_large.py
│   ├── extract_idioms.py
│   ├── filter_idiom_candidates.py
│   ├── prepare_idiom_review.py
│   ├── inspect_idiom_candidates.py
│   ├── inspect_verified_candidates.py
│   ├── prepare_idiom_training.py
│   ├── finetune_idiom_model.py
│   ├── evaluate_idiom_finetuned.py
│   ├── evaluate_unseen_idioms.py
│   ├── analyze_idiom_predictions.py
│   ├── analyze_final_idioms.py
│   ├── evaluate_meteor.py
│   └── create_final_comparison.py
│
├── README.md
├── ASSESSMENT_REPORT.md
├── requirements.txt
└── .gitignore

---

# 27. Reproducibility

The major project steps can be reproduced using the Python scripts in the src/ directory.

The general workflow is:

Dataset
   ↓
Dataset Inspection
   ↓
Dataset Preparation
   ↓
General Fine-Tuning
   ↓
Idiom Extraction
   ↓
Candidate Filtering
   ↓
Idiom Verification
   ↓
Idiom Training Dataset
   ↓
Idiom Fine-Tuning
   ↓
Evaluation
   ↓
Unseen Idiom Testing
   ↓
METEOR Evaluation
   ↓
FastAPI

---

# 28. Requirements

The project uses the following Python libraries:

torch
transformers
datasets
pandas
numpy
sacrebleu
sentencepiece
sacremoses
nltk
fastapi
uvicorn

---

# 29. Limitations

The current model is a specialized prototype rather than a production-scale translation system.

Important limitations include:

The idiom-specific dataset contains only 63 training examples.
Some idioms are still translated literally.
The unseen test contains only 15 examples.
BLEU and METEOR do not completely measure semantic correctness.
CPU inference can be slow.
The model requires additional data for stronger generalization.
Some culturally specific idioms require deeper contextual understanding.
The Render deployment encountered resource limitations while loading the
approximately 302 MB model on the available service environment.

The deployment limitation does not affect the successful local FastAPI implementation or the published Hugging Face model.

---

# 30. Future Improvements

Future versions could improve the system by:

1. Increasing the number of verified idiom examples.
2. Adding multiple contextual examples for each idiom.
3. Adding more high-quality human-reviewed English references.
4. Increasing the unseen evaluation dataset.
5. Performing human evaluation in addition to automatic metrics.
6. Experimenting with larger multilingual translation models.
7. Optimizing inference for CPU environments.
8. Using quantization to reduce memory usage.
9. Improving cloud deployment resources.
10. Creating a simple web interface for users.
11. Adding automatic idiom detection before translation.
12. Comparing several translation models.

---

# 31. Key Results

The most important completed results are:

General Translation Model

Validation examples: 1,999
BLEU: 88.44

Final Idiom-Specialized Model

Training examples: 63
BLEU: 14.16
METEOR: 32.43%
Average Word Overlap: 42.46%
Exact Matches: 1 / 63

Unseen Idiom Evaluation

Examples: 15
BLEU: 16.34
Average Word Overlap: 45.45%
Exact Matches: 0

Improvement After Idiom Fine-Tuning

BLEU:
7.85 → 14.16
Improvement: +6.31


Average Word Overlap:
37.59% → 42.46%
Improvement: +4.87 percentage points


Exact Matches:
0 → 1

---

# 32. Conclusion

This project successfully developed an end-to-end Hindi → English translation pipeline with additional specialization for Hindi idiomatic expressions.

A pretrained MarianMT model was first adapted using Hindi-English parallel data. A separate idiom-focused dataset was then created through extraction, filtering, review, and verification.

The verified idiom examples were used for additional fine-tuning.

The final idiom-specialized model achieved a BLEU score of **14.16**, compared with **7.85** before idiom-specific fine-tuning. Average word overlap also increased from **37.59% to 42.46%**, while the number of exact matches increased from **0 to 1**.

The final model additionally achieved a METEOR score of **32.43%** on the 63-example idiom evaluation set.

An unseen idiom test was also performed using 15 examples, achieving a BLEU score of **16.34** and average word overlap of **45.45%**.

The trained model was successfully exposed through a FastAPI REST API and uploaded to Hugging Face. The project source code and documentation were maintained using Git and GitHub.

Although the current model still has limitations because of the relatively small idiom-specific dataset, the project demonstrates the complete process of dataset preparation, transfer learning, domain-specific fine-tuning, evaluation, error analysis, API development, model publishing, and version control.

Overall, the project demonstrates a practical approach to improving neural machine translation for a specialized linguistic domain such as Hindi idiomatic expressions.
