from datasets import load_dataset
from transformers import (
    MarianMTModel,
    MarianTokenizer,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer
)

model_name = "Helsinki-NLP/opus-mt-hi-en"

print("Loading tokenizer...")
tokenizer = MarianTokenizer.from_pretrained(model_name)

print("Loading model...")
model = MarianMTModel.from_pretrained(model_name)

print("Loading large datasets...")

dataset = load_dataset(
    "csv",
    data_files={
        "train": "data/train_large.csv",
        "validation": "data/validation_large.csv"
    }
)

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

data_collator = DataCollatorForSeq2Seq(
    tokenizer=tokenizer,
    model=model
)

training_args = Seq2SeqTrainingArguments(
    output_dir="./large_results",
    eval_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    weight_decay=0.01,
    save_total_limit=2,
    num_train_epochs=1,
    predict_with_generate=True,
    logging_steps=500,
    report_to="none"
)

trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
    processing_class=tokenizer,
    data_collator=data_collator
)

print("Starting larger fine-tuning...")

trainer.train()

print("Saving larger fine-tuned model...")

trainer.save_model("./fine_tuned_large_model")
tokenizer.save_pretrained("./fine_tuned_large_model")

print("Larger fine-tuning completed successfully!")