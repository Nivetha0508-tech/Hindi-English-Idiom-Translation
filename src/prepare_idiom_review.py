import pandas as pd

input_file = "data/hindi_idiom_candidates.csv"
output_file = "data/idiom_review.csv"

df = pd.read_csv(input_file)

# Keep one representative sentence for each unique idiom
df_unique = df.drop_duplicates(subset=["idiom"]).copy()

# Add columns that we will fill during the review stage
df_unique["english_meaning"] = ""
df_unique["quality"] = ""
df_unique["notes"] = ""

# Put useful columns first
df_unique = df_unique[
    [
        "idiom",
        "sentence",
        "matched_span",
        "register",
        "region",
        "english_meaning",
        "quality",
        "notes"
    ]
]

df_unique.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("Idiom review file created successfully!")
print("Unique idioms:", len(df_unique))
print("Saved to:", output_file)