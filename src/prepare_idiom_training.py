import pandas as pd
import os

INPUT_FILE = "data/verified_hindi_english_idioms.csv"
OUTPUT_FILE = "data/idiom_training.csv"

# Load verified idiom dataset
df = pd.read_csv(INPUT_FILE)

print("=" * 70)
print("PREPARING IDIOM TRAINING DATA")
print("=" * 70)

print(f"Input rows: {len(df)}")

# Keep only the required translation columns
training_df = df[
    ["hindi_sentence", "english_translation"]
].copy()

# Rename columns for training
training_df.columns = ["source", "target"]

# Remove accidental duplicates
training_df = training_df.drop_duplicates()

# Remove missing values
training_df = training_df.dropna()

# Save
training_df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig"
)

print()
print(f"Training rows: {len(training_df)}")
print(f"Saved to: {OUTPUT_FILE}")

print()
print("Sample training examples:")
print("=" * 70)

for i, row in training_df.head(5).iterrows():
    print(f"\n{i + 1}. Hindi:")
    print(row["source"])
    print("English:")
    print(row["target"])

print()
print("=" * 70)
print("IDIOM TRAINING DATA PREPARATION COMPLETED")
print("=" * 70)