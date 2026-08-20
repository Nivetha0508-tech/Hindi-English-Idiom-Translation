from datasets import load_dataset
from transformers import (
    MarianMTModel,
    MarianTokenizer,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer
)

# -----------------------------
# 1. Load the model and tokenizer
# -----------------------------

model_name = "Helsinki-NLP/opus-mt-hi-en"

print("Loading tokenizer...")
tokenizer = MarianTokenizer.from_pretrained(model_name)

print("Loading model...")
model = MarianMTModel.from_pretrained(model_name)

# -----------------------------
# 2. Load our CSV datasets
# -----------------------------

print("Loading datasets...")

dataset = load_dataset(
    "csv",
    data_files={
        "train": "data/train.csv",
        "validation": "data/validation.csv"
    }
)

# -----------------------------
# 3. Remove missing values
# -----------------------------

print("Cleaning datasets...")

def valid_row(example):
    return (
        example["hindi"] is not None
        and example["english"] is not None
        and str(example["hindi"]).strip() != ""
        and str(example["english"]).strip() != ""
    )

dataset = dataset.filter(valid_row)

print(dataset)

# -----------------------------
# 4. Tokenize Hindi → English
# -----------------------------

def tokenize_function(examples):

    inputs = tokenizer(
        examples["hindi"],
        max_length=128,
        truncation=True
    )

    labels = tokenizer(
        text_target=examples["english"],
        max_length=128,
        truncation=True
    )

    inputs["labels"] = labels["input_ids"]

    return inputs


print("Tokenizing datasets...")

tokenized_dataset = dataset.map(
    tokenize_function,
    batched=True,
    remove_columns=["hindi", "english"]
)

print("Tokenization completed!")

# -----------------------------
# 5. Prepare batches
# -----------------------------

data_collator = DataCollatorForSeq2Seq(
    tokenizer=tokenizer,
    model=model
)

# -----------------------------
# 6. Training configuration
# -----------------------------

training_args = Seq2SeqTrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    weight_decay=0.01,
    save_total_limit=2,
    num_train_epochs=1,
    max_steps=100,
    predict_with_generate=True,
    logging_steps=10,
    report_to="none"
)

# -----------------------------
# 7. Create trainer
# -----------------------------

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
    processing_class=tokenizer,
    data_collator=data_collator
)

# -----------------------------
# 8. Start fine-tuning
# -----------------------------

print("Starting fine-tuning...")

trainer.train()

# -----------------------------
# 9. Save the fine-tuned model
# -----------------------------

print("Saving fine-tuned model...")

trainer.save_model("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")

print("Fine-tuning completed successfully!")