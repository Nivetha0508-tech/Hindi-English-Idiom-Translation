import pandas as pd

file_path = "data/verified_hindi_english_idioms.csv"

df = pd.read_csv(file_path)

print("Final verified idiom dataset")
print("=" * 50)

print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")

print("\nColumns:")
for column in df.columns:
    print(f"- {column}")

print("\nMissing values:")
print(df.isnull().sum())

print("\nAll verified idioms:")
print("=" * 50)

for index, row in df.iterrows():
    print(f"\n{index + 1}. {row['hindi_idiom']}")
    print(f"   Hindi: {row['hindi_sentence']}")
    print(f"   English: {row['english_translation']}")
    print(f"   Meaning: {row['idiom_meaning']}")

print("\n" + "=" * 50)
print("Dataset inspection completed.")