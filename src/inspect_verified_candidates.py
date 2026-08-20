import pandas as pd

file_path = "data/idiom_verified_candidates.csv"

df = pd.read_csv(file_path)

print("Total candidates:", len(df))
print("\nAll candidate idioms:\n")

for i, row in df.iterrows():
    print(f"{i + 1}. {row['idiom']}")
    print(f"   Sentence: {row['sentence']}")
    print()