from datasets import load_dataset
import csv
import random

print("Loading 50,000 Hindi-English pairs...")

# Load 50,000 examples from the original training dataset
dataset = load_dataset(
    "cfilt/iitb-english-hindi",
    split="train[:50000]"
)

# Extract Hindi → English pairs
data = []

for item in dataset:
    hindi = item["translation"]["hi"]
    english = item["translation"]["en"]

    # Keep only valid pairs
    if (
        hindi is not None
        and english is not None
        and str(hindi).strip() != ""
        and str(english).strip() != ""
    ):
        data.append({
            "hindi": hindi,
            "english": english
        })

# Shuffle the data
random.seed(42)
random.shuffle(data)

# Split the data
train_data = data[:48000]
validation_data = data[48000:]

# Save training data
with open(
    "data/train_large.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["hindi", "english"]
    )

    writer.writeheader()
    writer.writerows(train_data)

# Save validation data
with open(
    "data/validation_large.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["hindi", "english"]
    )

    writer.writeheader()
    writer.writerows(validation_data)

print("Large dataset preparation completed!")
print("Training pairs:", len(train_data))
print("Validation pairs:", len(validation_data))
print("Total valid pairs:", len(data))