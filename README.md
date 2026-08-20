# Hindi → English Idiom Translation Model

## 📌 Project Overview

This project develops a specialized Hindi → English neural machine translation
system using Hugging Face Transformers, MarianMT, and FastAPI.

The project started with a general Hindi → English translation model trained
using the IITB Hindi-English parallel dataset. After evaluating the general
translation model, the project was extended to specifically handle Hindi
idioms and their contextual meanings.

The final system combines:

- General Hindi → English translation capability
- Idiom-focused dataset preparation
- Verified Hindi idiom examples
- Idiom-specific fine-tuning
- Unseen idiom evaluation
- FastAPI REST API for translation

The goal is to translate Hindi sentences into natural English while improving
the handling of Hindi idioms whose literal word-by-word meanings can be
different from their intended meanings.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Build a Hindi → English neural translation model
- Fine-tune a pretrained Hindi → English translation model
- Evaluate translation quality using BLEU
- Identify Hindi idioms from translation data
- Create and verify an idiom-focused dataset
- Fine-tune the model specifically for Hindi idiom translation
- Test the model on unseen idiom examples
- Provide the trained model through a FastAPI REST API
- Make the translation system accessible through an API endpoint

---

## 🛠️ Technologies Used

- Python 3.11
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- MarianMT
- Pandas
- NumPy
- SacreBLEU
- SentencePiece
- Sacremoses
- FastAPI
- Uvicorn
- REST API
- Git & GitHub
- VS Code

---

# 📚 Dataset

The project uses the IITB Hindi-English parallel dataset available through
Hugging Face.

Dataset:

`cfilt/iitb-english-hindi`

The dataset provides Hindi-English parallel translation pairs.

The initial dataset was inspected to understand:

- Hindi source sentences
- English target translations
- Dataset structure
- Missing values
- Translation pair quality

A smaller sample was initially inspected before preparing the larger dataset.

---

# 🤖 Pretrained Translation Model

The pretrained model used in this project is:

`Helsinki-NLP/opus-mt-hi-en`

This model is based on the MarianMT architecture and is designed for
Hindi → English machine translation.

Instead of training a translation model from scratch, the pretrained model
was fine-tuned using Hindi-English parallel data.

---

# 🔄 Project Workflow

The project was developed in multiple stages.

## Stage 1 — Dataset Inspection

The IITB Hindi-English dataset was loaded and inspected to understand its
structure and translation pairs.

The initial inspection confirmed that the dataset contains Hindi source
sentences and corresponding English translations.

---

## Stage 2 — General Dataset Preparation

The Hindi-English data was cleaned and prepared for model training.

The project prepared a larger dataset containing:

- 50,000 selected Hindi-English pairs
- 48,000 training pairs
- 2,000 validation pairs

After removing invalid or missing translation entries:

- 47,985 training examples
- 1,999 validation examples

were used for model training and evaluation.

---

## Stage 3 — General Model Fine-Tuning

The pretrained MarianMT Hindi → English model was fine-tuned using the
prepared Hindi-English dataset.

The fine-tuned model was saved locally for further testing and evaluation.

---

## Stage 4 — General Translation Evaluation

The original pretrained model and the fine-tuned model were evaluated using
BLEU.

### Original Pretrained Model

BLEU Score:

**81.84**

### General Fine-Tuned Model

BLEU Score:

**88.44**

### Improvement

The fine-tuned model achieved an improvement of approximately:

**+6.60 BLEU points**

This showed that fine-tuning on the prepared Hindi-English dataset improved
translation performance on the validation data used in the project.

---

# 🧠 Idiom-Specific Translation Extension

After completing the general Hindi → English translation model, the project
was extended to focus specifically on Hindi idioms.

Hindi idioms can be difficult for translation systems because their literal
word meanings may not represent their actual contextual meaning.

For example:

Hindi idiom:

`अपना उल्लू सीधा करना`

Literal meaning:

"To straighten one's owl"

Contextual meaning:

"To serve one's own interests"

Therefore, the project created an idiom-focused translation pipeline.

---

# 🔍 Idiom Dataset Creation

The project processed the Hindi-English data to identify potential Hindi
idioms and idiomatic expressions.

The workflow included:

1. Extracting possible idiomatic expressions
2. Filtering candidate idioms
3. Reviewing candidate translations
4. Verifying idiom examples
5. Creating contextual Hindi sentences
6. Creating appropriate English translations
7. Preparing verified training examples

The project generated and reviewed multiple intermediate datasets during
this process.

Important files include:

```text
data/hindi_english_idioms.csv
data/hindi_idiom_candidates.csv
data/idiom_review.csv
data/idiom_verified_candidates.csv
data/verified_hindi_english_idioms.csv
```
---

# ✅ Verified Idiom Training Dataset

After the review and verification process, a final idiom-specific training dataset was created.

Final idiom training examples:

**63**

The dataset contains contextual Hindi sentences paired with their intended English translations.

Example:

Hindi
किसान सरकार से मदद के लिए हाथ जोड़कर गुहार लगा रहा था।
English
*The farmer was pleading with the government for help.*
---

# 🧠 Idiom-Specific Fine-Tuning

The existing general fine-tuned Hindi → English model was used as the starting point for idiom-specific fine-tuning.

This approach allows the model to retain its general Hindi → English
translation capability while further adapting it to the verified idiom examples.

The final idiom-specialized model was saved as:

*fine_tuned_idiom_model/*
---

# 📊 Idiom Model Evaluation

The idiom-specialized model was evaluated on the 63 verified idiom examples.

**Evaluation Results**
Metric      	        Result
Total Examples  	      63
Exact Matches   	      1
Average Word Overlap	42.46%
BLEU Score	            0.141581
BLEU Percentage	         14.16%

The results show that idiom-specific translation remains challenging, especially when the intended idiomatic meaning differs significantly from the literal meaning of the Hindi words.

The evaluation was therefore extended beyond the BLEU score to inspect individual predictions and word overlap
---

# 🔬 Idiom Prediction Analysis

The final predictions were analyzed individually to understand the model's behavior.

**The analysis classified predictions into:**

- High Word Overlap
- Partial Word Overlap
- Low Word Overlap

Results:

Category        	Examples
High Word Overlap	    17
Partial Word Overlap	27
Low Word Overlap	    19

The analysis demonstrated that the model often understands parts of the sentence correctly but may translate the idiom literally instead of producing its intended English meaning.

This analysis was used to understand the limitations of the current
idiom-specialized model rather than relying only on a single evaluation metric.

# 🧪 Unseen Idiom Evaluation

To check whether the model could generalize beyond the 63 training examples, a separate unseen idiom test set was created.

The unseen test set contained:

- 15 examples

These examples were not used during idiom-specific training.

**Unseen Test Results**
Metric              	Result
Total Examples 	          15
Exact Matches	          0
Average Word Overlap	45.45%
BLEU Score          	0.163432
BLEU Percentage     	16.34%

The unseen evaluation provides a more realistic indication of how the idiom-specialized model performs on idioms that were not directly included in its training examples.
---

# ⚠️ Current Model Limitations

The current idiom-specialized model is a working research prototype and has several limitations.

**The main limitations are:**

- The idiom-specific training dataset is relatively small.
- Some idioms are translated too literally.
- Exact idiomatic English equivalents are not always generated.
- Some predictions preserve sentence-level meaning but lose the idiomatic meaning.
- BLEU is relatively low for the idiom-specific evaluation set.
- Unseen idioms remain challenging.
- More high-quality verified idiom examples would likely improve performance.

These limitations are documented intentionally as part of the model
evaluation.
---

# 🚀 FastAPI Application

The trained idiom-specialized model is exposed through a FastAPI REST API.

The API loads:

*fine_tuned_idiom_model/*

and provides Hindi → English translation functionality.

The API application is located at:

*api/main.py*
---

# 🌐 API Endpoints
Health Check
*GET /health*

This endpoint verifies that the API and translation model are running.

Example response:

{
  "status": "healthy"
}

Translation Endpoint
*POST /translate*

This endpoint accepts a Hindi sentence and returns its English translation.

Example request:

{
  "text": "किसान सरकार से मदद के लिए हाथ जोड़कर गुहार लगा रहा था।"
}

Example response:

{
  "translation": "The farmer was pleading with the government for help."
}

**API Documentation**

FastAPI automatically provides interactive API documentation.

Swagger UI:

http://127.0.0.1:8000/docs

OpenAPI specification:

http://127.0.0.1:8000/openapi.json
---

# ▶️ Running the API

Activate the virtual environment:

*.\venv\Scripts\Activate.ps1*

Start the FastAPI server:

*uvicorn api.main:app --reload*

The API will run at:

http://127.0.0.1:8000

The interactive Swagger documentation can then be opened at:

http://127.0.0.1:8000/docs
---

# 📦 Python Dependencies

The project uses the following major dependencies:

1. torch
2. transformers
3. datasets
4. pandas
5. numpy
6. sacrebleu
7. sentencepiece
8. sacremoses
9. fastapi
10. uvicorn

They are also listed in:

*requirements.txt*
---

# 📁 Project Structure

Translation-Model-FineTuning/
│
├── api/
│   └── main.py
│
├── data/
│   ├── hindi_english.csv
│   ├── train.csv
│   ├── validation.csv
│   ├── train_large.csv
│   ├── validation_large.csv
│   │
│   ├── hindi_english_idioms.csv
│   ├── hindi_idiom_candidates.csv
│   ├── idiom_review.csv
│   ├── idiom_verified_candidates.csv
│   ├── idiom_training.csv
│   ├── verified_hindi_english_idioms.csv
│   ├── unseen_idiom_test.csv
│   ├── final_idiom_predictions.csv
│   └── final_idiom_analysis.csv
│
├── fine_tuned_model/
│
├── fine_tuned_large_model/
│
├── fine_tuned_idiom_model/
│   ├── config.json
│   ├── generation_config.json
│   ├── model.safetensors
│   ├── source.spm
│   ├── target.spm
│   ├── tokenizer_config.json
│   ├── training_args.bin
│   └── vocab.json
│
├── model/
│
├── results/
│
├── large_results/
│
├── src/
│   ├── check_dataset.py
│   ├── check_training_data.py
│   ├── compare_models.py
│   ├── create_verified_idiom_dataset.py
│   ├── evaluate_idiom_finetuned.py
│   ├── evaluate_model.py
│   ├── evaluate_unseen_idioms.py
│   ├── evaluate_verified_idioms.py
│   ├── extract_idioms.py
│   ├── filter_idiom_candidates.py
│   ├── fine_tune.py
│   ├── fine_tune_large.py
│   ├── finetune_idiom_model.py
│   ├── inspect_final_idiom_dataset.py
│   ├── inspect_idiom_candidates.py
│   ├── inspect_idioms.py
│   ├── inspect_verified_candidates.py
│   ├── load_model.py
│   ├── prepare_dataset.py
│   ├── prepare_idiom_review.py
│   ├── prepare_idiom_training.py
│   ├── prepare_large_dataset.py
│   ├── test_fine_tuned.py
│   ├── test_large_model.py
│   ├── test_translation.py
│   ├── train_model.py
│   ├── translation_demo.py
│   └── validate_final_idiom_dataset.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── venv/
---

# 📌 Important Generated Models

The project contains multiple stages of trained models.

Base pretrained model
*Helsinki-NLP/opus-mt-hi-en*
General fine-tuned model
*fine_tuned_model/*
Larger general fine-tuned model
*fine_tuned_large_model/*
Final idiom-specialized model
*fine_tuned_idiom_model/*

The final FastAPI application uses:

*fine_tuned_idiom_model/*
---

# 🔐 Git and Version Control

Git is used to track the project source code, datasets, API code, scripts, configuration files, and documentation.

The project includes a .gitignore file to prevent unnecessary files such as the Python virtual environment, Python cache files, VS Code settings, and training checkpoint directories from being tracked.

Example ignored directories:
- venv/
- __pycache__/
- .vscode/
- results/checkpoint-*/
- large_results/checkpoint-*/
---

# 📈 Overall Results

The project successfully completed both general Hindi → English translation and idiom-focused translation stages.

- General Translation Model
**Validation Examples : 1,999**
**BLEU Score          : 88.44**

The general fine-tuned model showed a significant improvement over the pretrained model.

- Idiom-Specialized Model
**Training Examples   : 63**
**BLEU Score          : 14.16%**
**Unseen Test Examples: 15**
**Unseen BLEU         : 16.34%**

The idiom-specific results show that translating idioms correctly is more challenging than general sentence translation and that a larger, more diverse, and higher-quality idiom dataset would be beneficial for future improvements.
---

# 🎯 Final System

The completed system follows this pipeline:

Hindi Input
     │
     ▼
FastAPI API
     │
     ▼
Hindi Tokenization
     │
     ▼
Idiom-Specialized MarianMT Model
     │
     ▼
English Translation
     │
     ▼
API Response
---

# 🔮 Future Improvements

Possible future improvements include:

- Increase the number of verified Hindi idiom training examples
- Add multiple contextual examples for each idiom
- Include more diverse Hindi-English idiomatic expressions
- Improve English reference translations
- Experiment with different fine-tuning strategies
- Compare multiple pretrained translation models
- Improve unseen idiom generalization
- Add confidence or quality indicators
- Build a simple frontend for the FastAPI service
- Deploy the API as a cloud service
- Add automated API testing
- Add more comprehensive evaluation metrics
---

# 🏁 Conclusion

This project demonstrates the complete development of a Hindi → English translation system, starting from a pretrained neural machine translation model and progressing through dataset preparation, fine-tuning, evaluation, idiom extraction, idiom verification, idiom-specific fine-tuning, unseen testing, and API integration.

The general Hindi → English model achieved a BLEU score of **88.44** on the validation dataset after fine-tuning.

The project was then extended into an idiom-focused translation system using verified contextual Hindi idiom examples. The final idiom-specialized model was evaluated on both known and unseen idiom examples and exposed through a FastAPI REST API.

Although idiom translation remains challenging, the project provides a complete end-to-end foundation for developing and serving a specialized Hindi → English idiom translation model.

The project demonstrates practical experience with:

- Natural Language Processing
- Neural Machine Translation
- Transformer Models
- MarianMT
- Dataset Preparation
- Model Fine-Tuning
- Idiom Detection and Verification
- BLEU Evaluation
- Model Analysis
- FastAPI
- REST APIs
- Python
- Git and Version Control

*This is the version I recommend using now.** It reflects what you actually completed rather than presenting the project as only a general translation model.*
