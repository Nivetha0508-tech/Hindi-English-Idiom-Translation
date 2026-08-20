from datasets import load_dataset
from transformers import MarianMTModel, MarianTokenizer

# Model name
model_name = "Helsinki-NLP/opus-mt-hi-en"

print("Loading tokenizer...")
tokenizer = MarianTokenizer.from_pretrained(model_name)

print("Loading model...")
model = MarianMTModel.from_pretrained(model_name)

# Load our prepared CSV files
print("Loading training and validation data...")

dataset = load_dataset(
    "csv",
    data_files={
        "train": "data/train.csv",
        "validation": "data/validation.csv"
    }
)

print(dataset)

# Remove rows where Hindi or English is missing
print("Removing rows with missing translations...")

def valid_row(example):
    return (
        example["hindi"] is not None
        and example["english"] is not None
        and str(example["hindi"]).strip() != ""
        and str(example["english"]).strip() != ""
    )

dataset = dataset.filter(valid_row)

print("Dataset after cleaning:")
print(dataset)

# Tokenize the data
def tokenize_function(examples):
    model_inputs = tokenizer(
        examples["hindi"],
        max_length=128,
        truncation=True
    )

    labels = tokenizer(
        text_target=examples["english"],
        max_length=128,
        truncation=True
    )

    model_inputs["labels"] = labels["input_ids"]

    return model_inputs

print("Tokenizing training data...")

tokenized_dataset = dataset.map(
    tokenize_function,
    batched=True
)

print("Tokenization completed!")

print("Training examples:", len(tokenized_dataset["train"]))
print("Validation examples:", len(tokenized_dataset["validation"]))