from datasets import load_dataset

print("Loading Hindi idiom dataset...")

dataset = load_dataset(
    "Justarandomperson/MultIdiom_Dataset",
    split="train"
)

print("\nDataset loaded!")
print(dataset)

# Keep only Hindi examples
hindi_dataset = dataset.filter(
    lambda x: x["language"] == "Hindi"
)

print("\nHindi examples:")
print(hindi_dataset)

print("\nNumber of Hindi examples:", len(hindi_dataset))

print("\nFirst 10 Hindi idiom examples:\n")

for i in range(min(10, len(hindi_dataset))):
    item = hindi_dataset[i]

    print("Idiom:", item["idiom"])
    print("Meaning ID:", item["meaning_id"])
    print("Idiomaticity:", item["idiomaticity"])
    print("Sentence:", item["sentence"])
    print("Matched span:", item["matched_span"])
    print("-" * 70)