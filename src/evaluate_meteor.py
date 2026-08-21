import pandas as pd
from nltk.translate.meteor_score import meteor_score


# ============================================================
# CONFIGURATION
# ============================================================

INPUT_FILE = "data/final_idiom_predictions.csv"

REFERENCE_COLUMN = "english_translation"
PREDICTION_COLUMN = "model_prediction"

OUTPUT_FILE = "data/final_idiom_meteor.csv"


# ============================================================
# LOAD DATA
# ============================================================

print("=" * 70)
print("METEOR EVALUATION - FINAL IDIOM MODEL")
print("=" * 70)

df = pd.read_csv(INPUT_FILE)

print(f"Total examples: {len(df)}")
print(f"Columns found: {list(df.columns)}")


# ============================================================
# CHECK REQUIRED COLUMNS
# ============================================================

required_columns = [
    REFERENCE_COLUMN,
    PREDICTION_COLUMN
]

for column in required_columns:

    if column not in df.columns:

        raise ValueError(
            f"Required column '{column}' not found.\n"
            f"Available columns: {list(df.columns)}"
        )


# ============================================================
# CALCULATE METEOR SCORES
# ============================================================

meteor_scores = []

for _, row in df.iterrows():

    reference = str(row[REFERENCE_COLUMN]).strip()
    prediction = str(row[PREDICTION_COLUMN]).strip()

    reference_tokens = reference.lower().split()
    prediction_tokens = prediction.lower().split()

    if not reference_tokens or not prediction_tokens:

        score = 0.0

    else:

        score = meteor_score(
            [reference_tokens],
            prediction_tokens
        )

    meteor_scores.append(score)


# ============================================================
# ADD SCORES TO DATAFRAME
# ============================================================

df["meteor_score"] = meteor_scores


# ============================================================
# SAVE RESULTS
# ============================================================

df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig"
)


# ============================================================
# FINAL METEOR RESULT
# ============================================================

average_meteor = sum(meteor_scores) / len(meteor_scores)

print()
print("=" * 70)
print("FINAL METEOR RESULT")
print("=" * 70)

print(f"Total examples : {len(meteor_scores)}")
print(f"METEOR score   : {average_meteor:.6f}")
print(f"METEOR percent : {average_meteor * 100:.2f}%")

print("=" * 70)

print()
print("METEOR evaluation completed successfully.")
print(f"Results saved to: {OUTPUT_FILE}")