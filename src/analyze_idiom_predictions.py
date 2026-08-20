import pandas as pd
import re

INPUT_PATH = "data/verified_idiom_predictions.csv"
OUTPUT_PATH = "data/idiom_prediction_analysis.csv"

df = pd.read_csv(INPUT_PATH)


def normalize(text):
    text = str(text).lower().strip()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text


def word_overlap(reference, prediction):
    ref_words = set(normalize(reference).split())
    pred_words = set(normalize(prediction).split())

    if not ref_words:
        return 0.0

    return len(ref_words & pred_words) / len(ref_words)


# ------------------------------------------------------------
# ANALYSIS
# ------------------------------------------------------------

df["normalized_reference"] = df["english_translation"].apply(normalize)
df["normalized_prediction"] = df["model_prediction"].apply(normalize)

df["exact_match"] = (
    df["normalized_reference"] == df["normalized_prediction"]
)

df["word_overlap"] = df.apply(
    lambda row: word_overlap(
        row["english_translation"],
        row["model_prediction"]
    ),
    axis=1
)

# Simple automatic category.
# This is only a preliminary classification.
def preliminary_category(row):
    if row["exact_match"]:
        return "Exact Match"
    elif row["word_overlap"] >= 0.50:
        return "High Word Overlap"
    elif row["word_overlap"] >= 0.25:
        return "Partial Word Overlap"
    else:
        return "Low Word Overlap"


df["preliminary_category"] = df.apply(
    preliminary_category,
    axis=1
)

# ------------------------------------------------------------
# SAVE ANALYSIS
# ------------------------------------------------------------

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

print("=" * 70)
print("IDIOM PREDICTION ANALYSIS")
print("=" * 70)

print(f"\nTotal examples: {len(df)}")

print(
    f"Exact matches: "
    f"{df['exact_match'].sum()}"
)

print(
    f"Average word overlap: "
    f"{df['word_overlap'].mean():.2%}"
)

print("\nPreliminary categories:")
print(
    df["preliminary_category"]
    .value_counts()
)

# ------------------------------------------------------------
# PRINT EVERY PREDICTION
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("EXPECTED vs MODEL PREDICTION")
print("=" * 70)

for _, row in df.iterrows():

    print(f"\n{row['id']}. {row['hindi_idiom']}")

    print(f"   Hindi:")
    print(f"   {row['hindi_sentence']}")

    print(f"\n   Expected:")
    print(f"   {row['english_translation']}")

    print(f"\n   Model prediction:")
    print(f"   {row['model_prediction']}")

    print(f"\n   Word overlap: {row['word_overlap']:.2%}")
    print(f"   Preliminary: {row['preliminary_category']}")

print("\n" + "=" * 70)
print("Analysis saved to:")
print(OUTPUT_PATH)
print("=" * 70)