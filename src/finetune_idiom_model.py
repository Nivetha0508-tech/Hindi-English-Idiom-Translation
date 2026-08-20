import os
import pandas as pd

from datasets import Dataset
from transformers import (
    MarianMTModel,
    MarianTokenizer,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    DataCollatorForSeq2Seq
)


# ============================================================
# CONFIGURATION
# ============================================================

BASE_MODEL_PATH = "fine_tuned_large_model"
DATA_PATH = "data/idiom_training.csv"
OUTPUT_DIR = "fine_tuned_idiom_model"


# ============================================================
# HEADER
# ============================================================

print("=" * 70)
print("LOADING VERIFIED IDIOM TRAINING DATA")
print("=" * 70)


# ============================================================
# LOAD TRAINING DATA
# ============================================================

df = pd.read_csv(DATA_PATH)

print(f"Total training examples: {len(df)}")


# Check required columns
required_columns = ["source", "target"]

for column in required_columns:
    if column not in df.columns:
        raise ValueError(
            f"Required column '{column}' not found in {DATA_PATH}"
        )


# Remove missing values
df = df.dropna(
    subset=["source", "target"]
).reset_index(drop=True)

print(f"Valid training examples: {len(df)}")


# ============================================================
# CREATE HUGGING FACE DATASET
# ============================================================

dataset = Dataset.from_pandas(
    df[["source", "target"]],
    preserve_index=False
)


# ============================================================
# LOAD EXISTING FINE-TUNED MODEL
# ============================================================

print()
print("=" * 70)
print("LOADING EXISTING FINE-TUNED MODEL")
print("=" * 70)

print(f"Model: {BASE_MODEL_PATH}")


tokenizer = MarianTokenizer.from_pretrained(
    BASE_MODEL_PATH
)

model = MarianMTModel.from_pretrained(
    BASE_MODEL_PATH
)


# ============================================================
# TOKENIZATION
# ============================================================

print()
print("=" * 70)
print("TOKENIZING IDIOM DATA")
print("=" * 70)


def tokenize_function(examples):

    model_inputs = tokenizer(
        examples["source"],
        max_length=128,
        truncation=True
    )

    labels = tokenizer(
        text_target=examples["target"],
        max_length=128,
        truncation=True
    )

    model_inputs["labels"] = labels["input_ids"]

    return model_inputs


tokenized_dataset = dataset.map(
    tokenize_function,
    batched=True,
    remove_columns=dataset.column_names
)

print("Tokenization completed.")


# ============================================================
# DATA COLLATOR
# ============================================================

data_collator = DataCollatorForSeq2Seq(
    tokenizer=tokenizer,
    model=model
)


# ============================================================
# TRAINING ARGUMENTS
# ============================================================

print()
print("=" * 70)
print("CONFIGURING IDIOM-SPECIFIC FINE-TUNING")
print("=" * 70)


training_args = Seq2SeqTrainingArguments(

    output_dir=OUTPUT_DIR,

    num_train_epochs=2,

    per_device_train_batch_size=4,

    learning_rate=2e-5,

    logging_steps=10,

    save_strategy="epoch",

    report_to="none",

    fp16=False,

    dataloader_pin_memory=False,

    remove_unused_columns=True
)


# ============================================================
# TRAINER
# ============================================================

trainer = Seq2SeqTrainer(

    model=model,

    args=training_args,

    train_dataset=tokenized_dataset,

    data_collator=data_collator
)


# ============================================================
# START TRAINING
# ============================================================

print()
print("=" * 70)
print("STARTING IDIOM-SPECIFIC FINE-TUNING")
print("=" * 70)

trainer.train()


# ============================================================
# SAVE MODEL
# ============================================================

print()
print("=" * 70)
print("SAVING IDIOM-SPECIALIZED MODEL")
print("=" * 70)


os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


trainer.save_model(
    OUTPUT_DIR
)

tokenizer.save_pretrained(
    OUTPUT_DIR
)


# ============================================================
# COMPLETION
# ============================================================

print()
print("=" * 70)
print("IDIOM-SPECIFIC FINE-TUNING COMPLETED")
print("=" * 70)

print(f"Model saved to: {OUTPUT_DIR}")
print(f"Training examples used: {len(tokenized_dataset)}")

print("=" * 70)