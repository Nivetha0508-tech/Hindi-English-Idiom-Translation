# Hindi → English Translation Model

## 📌 Project Overview

This project develops a Hindi → English neural machine translation model using
Hugging Face Transformers and the MarianMT architecture.

The main goal is to fine-tune a pretrained Hindi → English translation model
using a larger Hindi-English parallel dataset and evaluate whether fine-tuning
improves translation performance.

---

## 🎯 Objective

The objective of this project is to build a model that can:

- Accept a Hindi sentence as input
- Translate the Hindi sentence into English
- Learn from Hindi-English parallel training data
- Evaluate translation quality using the BLEU score
- Compare the fine-tuned model with the original pretrained model

---

## 🛠️ Technologies Used

- Python 3.11
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- MarianMT
- SacreBLEU
- Pandas
- NumPy
- VS Code

---

## 📚 Dataset

The project uses the IITB Hindi-English parallel dataset from Hugging Face.

Dataset:

`cfilt/iitb-english-hindi`

The dataset contains Hindi-English translation pairs.

The project initially inspected 100 examples to understand the dataset
structure before preparing the training data.

The final dataset preparation used:

- 50,000 valid Hindi-English pairs
- 48,000 training pairs
- 2,000 validation pairs

After removing missing translations:

- 47,985 training examples
- 1,999 validation examples

---

## 🤖 Pretrained Model

The pretrained model used for this project is:

`Helsinki-NLP/opus-mt-hi-en`

This model is designed for Hindi → English translation.

Instead of building a translation model from zero, the pretrained model was
fine-tuned using the prepared Hindi-English dataset.

---

## 🔄 Project Workflow

The project follows these main steps:

1. Load the Hindi-English dataset
2. Inspect the dataset structure
3. Extract Hindi → English translation pairs
4. Prepare the training and validation datasets
5. Clean missing translation entries
6. Load the pretrained MarianMT model
7. Load the Marian tokenizer
8. Tokenize Hindi input and English target sentences
9. Fine-tune the pretrained model
10. Save the fine-tuned model
11. Test the model using new Hindi sentences
12. Evaluate the model using BLEU
13. Compare the original and fine-tuned models
14. Create an interactive Hindi → English translation demo

---

## 📊 Dataset Split

| Dataset | Number of Examples |
|---|---:|
| Training | 47,985 |
| Validation | 1,999 |
| Total Valid | 49,984 |

---

## 📈 Model Evaluation

The model was evaluated using the BLEU score.

### Original Pretrained Model

BLEU Score:

**81.84**

### Fine-Tuned Model

BLEU Score:

**88.44**

### Improvement

The fine-tuned model improved the BLEU score by approximately:

**6.60 BLEU points**

This indicates that fine-tuning improved performance on the validation
dataset used in this project.

---

## 🧪 Sample Translation Results

The fine-tuned model was tested with new Hindi sentences.

### Example 1

**Hindi:**

मुझे आज बहुत खुशी हो रही है।

**English:**

I'm very happy today.

---

### Example 2

**Hindi:**

भारत एक सुंदर देश है।

**English:**

India is a pretty country.

---

### Example 3

**Hindi:**

मुझे नई चीजें सीखना पसंद है।

**English:**

I like to learn new things.

---

### Example 4

**Hindi:**

कृपया दरवाजा बंद करें।

**English:**

Please close the door.

---

## 📁 Project Structure

```text
Translation-Model-FineTuning/
│
├── data/
│   ├── hindi_english.csv
│   ├── train.csv
│   ├── validation.csv
│   ├── train_large.csv
│   └── validation_large.csv
│
├── fine_tuned_large_model/
│   ├── config.json
│   ├── generation_config.json
│   ├── model.safetensors
│   ├── source.spm
│   ├── target.spm
│   ├── tokenizer_config.json
│   ├── training_args.bin
│   └── vocab.json
│
├── fine_tuned_model/
├── large_results/
├── model/
├── results/
│
├── src/
│   ├── check_dataset.py
│   ├── check_training_data.py
│   ├── compare_models.py
│   ├── evaluate_model.py
│   ├── fine_tune.py
│   ├── fine_tune_large.py
│   ├── load_model.py
│   ├── prepare_dataset.py
│   ├── prepare_large_dataset.py
│   ├── test_fine_tuned.py
│   ├── test_large_model.py
│   ├── test_translation.py
│   ├── train_model.py
│   └── translation_demo.py
│
├── README.md
└── venv/