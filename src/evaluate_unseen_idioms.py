import os
import pandas as pd
import torch

from transformers import MarianMTModel, MarianTokenizer
from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_PATH = "fine_tuned_idiom_model"
INPUT_FILE = "data/unseen_idiom_test.csv"
OUTPUT_FILE = "data/unseen_idiom_predictions.csv"


# ============================================================
# LOAD DATA
# ============================================================

print("=" * 70)
print("LOADING UNSEEN IDIOM TEST DATA")
print("=" * 70)

df = pd.read_csv(INPUT_FILE)

print(f"Total unseen examples: {len(df)}")

required_columns = ["source", "target"]

for column in required_columns:
    if column not in df.columns:
        raise ValueError(
            f"Required column '{column}' not found in {INPUT_FILE}"
        )


# ============================================================
# LOAD MODEL
# ============================================================

print("\n" + "=" * 70)
print("LOADING IDIOM-SPECIALIZED MODEL")
print("=" * 70)

print(f"Model: {MODEL_PATH}")

tokenizer = MarianTokenizer.from_pretrained(MODEL_PATH)
model = MarianMTModel.from_pretrained(MODEL_PATH)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

print(f"Device: {device}")


# ============================================================
# GENERATE PREDICTIONS
# ============================================================

print("\n" + "=" * 70)
print("GENERATING UNSEEN IDIOM TRANSLATIONS")
print("=" * 70)

predictions = []

for index, row in df.iterrows():

    source_text = str(row["source"])

    inputs = tokenizer(
        source_text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=128
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    with torch.no_grad():

        generated_ids = model.generate(
            **inputs,
            max_length=128,
            num_beams=4,
            early_stopping=True
        )

    prediction = tokenizer.decode(
        generated_ids[0],
        skip_special_tokens=True
    )

    predictions.append(prediction)

    print(f"\n{index + 1}.")
    print("Hindi    :", source_text)
    print("Expected :", row["target"])
    print("Predicted:", prediction)


# ============================================================
# SAVE PREDICTIONS
# ============================================================

df["prediction"] = predictions

df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig"
)

print("\n" + "=" * 70)
print("PREDICTIONS SAVED")
print("=" * 70)

print(f"Saved to: {OUTPUT_FILE}")


# ============================================================
# BLEU SCORE
# ============================================================

references = [
    [str(target).lower().split()]
    for target in df["target"]
]

hypotheses = [
    str(prediction).lower().split()
    for prediction in df["prediction"]
]

smoothie = SmoothingFunction().method1

bleu_score = corpus_bleu(
    references,
    hypotheses,
    smoothing_function=smoothie
)


# ============================================================
# EXACT MATCH
# ============================================================

exact_matches = 0

for expected, prediction in zip(
    df["target"],
    df["prediction"]
):

    expected_clean = " ".join(
        str(expected).lower().split()
    )

    prediction_clean = " ".join(
        str(prediction).lower().split()
    )

    if expected_clean == prediction_clean:
        exact_matches += 1


# ============================================================
# WORD OVERLAP
# ============================================================

overlap_scores = []

for expected, prediction in zip(
    df["target"],
    df["prediction"]
):

    expected_words = set(
        str(expected).lower().split()
    )

    prediction_words = set(
        str(prediction).lower().split()
    )

    if len(expected_words) == 0:
        overlap = 0.0

    else:
        common_words = (
            expected_words.intersection(prediction_words)
        )

        overlap = (
            len(common_words) /
            len(expected_words)
        ) * 100

    overlap_scores.append(overlap)


average_overlap = sum(overlap_scores) / len(
    overlap_scores
)


# ============================================================
# FINAL RESULT
# ============================================================

print("\n" + "=" * 70)
print("UNSEEN IDIOM TEST RESULT")
print("=" * 70)

print(f"Total examples       : {len(df)}")
print(f"Exact matches        : {exact_matches}")
print(f"Average word overlap : {average_overlap:.2f}%")
print(f"BLEU score           : {bleu_score:.6f}")
print(f"BLEU percentage      : {bleu_score * 100:.2f}%")

print("=" * 70)
print("Unseen evaluation completed successfully.")
print("=" * 70)