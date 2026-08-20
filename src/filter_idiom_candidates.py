import pandas as pd

input_file = "data/idiom_review.csv"
output_file = "data/idiom_verified_candidates.csv"

df = pd.read_csv(input_file)

# Obvious generic/non-idiomatic expressions that should not be used
remove_idioms = {
    "खाना",
    "जलन",
    "जाग जाना",
    "जैसा कि मैं कह रहा था",
    "चढ़ जाना",
    "खबर लेना",
    "ख़बर लेना",
    "थककर बैठ जाना",
    "क्या मैं फ़ारसी बोल रहा हूँ",
}

# Remove obvious noisy entries
clean_df = df[~df["idiom"].isin(remove_idioms)].copy()

# Reset numbering
clean_df = clean_df.reset_index(drop=True)

clean_df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("Candidate filtering completed!")
print("Original unique idioms:", len(df))
print("Remaining candidates:", len(clean_df))
print("Removed:", len(df) - len(clean_df))
print("Saved to:", output_file)

print("\nFirst 20 remaining candidates:\n")

for i, row in clean_df.head(20).iterrows():
    print(f"{i + 1}. {row['idiom']}")