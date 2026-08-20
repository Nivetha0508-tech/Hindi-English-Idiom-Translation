from datasets import load_dataset
import csv

# Load 10,000 Hindi-English training examples
dataset = load_dataset(
    "cfilt/iitb-english-hindi",
    split="train[:10000]"
)

# Extract Hindi → English pairs
data = []

for item in dataset:
    hindi = item["translation"]["hi"]
    english = item["translation"]["en"]

    data.append({
        "hindi": hindi,
        "english": english
    })

# Shuffle the data
import random
random.shuffle(data)

# Split into training and validation data
train_data = data[:9000]
validation_data = data[9000:]

# Save training data
with open("data/train.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["hindi", "english"])
    writer.writeheader()
    writer.writerows(train_data)

# Save validation data
with open("data/validation.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["hindi", "english"])
    writer.writeheader()
    writer.writerows(validation_data)

print("Dataset preparation completed!")
print("Training pairs:", len(train_data))
print("Validation pairs:", len(validation_data))