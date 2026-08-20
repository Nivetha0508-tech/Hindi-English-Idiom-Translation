import pandas as pd
import re


# ============================================================
# CONFIGURATION
# ============================================================

INPUT_PATH = "data/final_idiom_predictions.csv"
OUTPUT_PATH = "data/final_idiom_analysis.csv"


# ============================================================
# HEADER
# ============================================================

print("=" * 70)
print("FINAL IDIOM PREDICTION ANALYSIS")
print("=" * 70)


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(INPUT_PATH)

print(f"Total examples: {len(df)}")


# ============================================================
# WORD OVERLAP FUNCTION
# ============================================================

def calculate_word_overlap(expected, prediction):

    expected_words = set(
        re.findall(r"\b[a-zA-Z]+\b", str(expected).lower())
    )

    prediction_words = set(
        re.findall(r"\b[a-zA-Z]+\b", str(prediction).lower())
    )

    if not expected_words:
        return 0.0

    common_words = expected_words.intersection(prediction_words)

    return (len(common_words) / len(expected_words)) * 100


# ============================================================
# ANALYSIS
# ============================================================

overlaps = []
categories = []
exact_matches = []


for _, row in df.iterrows():

    expected = str(row["english_translation"]).strip().lower()
    prediction = str(row["model_prediction"]).strip().lower()

    overlap = calculate_word_overlap(
        expected,
        prediction
    )

    overlaps.append(overlap)

    exact = expected == prediction

    exact_matches.append(exact)

    if overlap >= 60:
        category = "High Word Overlap"
    elif overlap >= 30:
        category = "Partial Word Overlap"
    else:
        category = "Low Word Overlap"

    categories.append(category)


# ============================================================
# ADD RESULTS
# ============================================================

df["word_overlap"] = overlaps
df["exact_match"] = exact_matches
df["category"] = categories


# ============================================================
# SUMMARY
# ============================================================

exact_count = sum(exact_matches)

average_overlap = sum(overlaps) / len(overlaps)


print()
print("=" * 70)
print("FINAL ANALYSIS SUMMARY")
print("=" * 70)

print(f"Total examples       : {len(df)}")
print(f"Exact matches        : {exact_count}")
print(f"Average word overlap : {average_overlap:.2f}%")


print()
print("Categories:")
print(
    df["category"].value_counts()
)


# ============================================================
# DETAILED RESULTS
# ============================================================

print()
print("=" * 70)
print("EXPECTED vs FINAL MODEL PREDICTION")
print("=" * 70)


for index, row in df.iterrows():

    print()
    print(f"{index + 1}. {row['hindi_idiom']}")

    print("   Hindi:")
    print(f"   {row['hindi_sentence']}")

    print()
    print("   Expected:")
    print(f"   {row['english_translation']}")

    print()
    print("   Final model prediction:")
    print(f"   {row['model_prediction']}")

    print()
    print(f"   Word overlap: {row['word_overlap']:.2f}%")
    print(f"   Category: {row['category']}")

    print("-" * 70)


# ============================================================
# SAVE ANALYSIS
# ============================================================

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)


print()
print("=" * 70)
print("ANALYSIS SAVED")
print("=" * 70)

print(f"Saved to: {OUTPUT_PATH}")

print("=" * 70)