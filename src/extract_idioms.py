from datasets import load_dataset
import csv

print("Loading MultiIdiom dataset...")

dataset = load_dataset(
    "Justarandomperson/MultIdiom_Dataset",
    split="train"
)

# Keep only Hindi examples that are actually idiomatic
hindi_idioms = dataset.filter(
    lambda x: (
        x["language"] == "Hindi"
        and x["idiomaticity"] == "idiomatic"
    )
)

print("Hindi idiomatic examples:", len(hindi_idioms))

output_file = "data/hindi_idiom_candidates.csv"

with open(output_file, "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)

    writer.writerow([
        "idiom",
        "sentence",
        "matched_span",
        "register",
        "region"
    ])

    for item in hindi_idioms:
        writer.writerow([
            item["idiom"],
            item["sentence"],
            item["matched_span"],
            item["register"],
            item["region"]
        ])

print("\nIdioms extracted successfully!")
print("Saved to:", output_file)