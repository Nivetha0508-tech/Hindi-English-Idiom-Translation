import pandas as pd

file_path = "data/hindi_idiom_candidates.csv"

df = pd.read_csv(file_path)

print("Total idiomatic examples:", len(df))
print("Unique idioms:", df["idiom"].nunique())

print("\nFirst 30 idiomatic examples:\n")

for i, row in df.head(30).iterrows():
    print(f"#{i + 1}")
    print("Idiom:", row["idiom"])
    print("Sentence:", row["sentence"])
    print("Matched span:", row["matched_span"])
    print("-" * 70)