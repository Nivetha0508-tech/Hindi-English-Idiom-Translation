import pandas as pd
from datasets import Dataset
from transformers import MarianMTModel, MarianTokenizer
from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_PATH = "fine_tuned_idiom_model"
DATA_PATH = "data/verified_hindi_english_idioms.csv"
OUTPUT_PATH = "data/final_idiom_predictions.csv"


# ============================================================
# HEADER
# ============================================================

print("=" * 70)
print("EVALUATING IDIOM-SPECIALIZED MODEL")
print("=" * 70)


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(DATA_PATH)

print(f"Total verified idioms: {len(df)}")


# ============================================================
# LOAD MODEL
# ============================================================

print()
print("=" * 70)
print("LOADING IDIOM-SPECIALIZED MODEL")
print("=" * 70)

print(f"Model: {MODEL_PATH}")

tokenizer = MarianTokenizer.from_pretrained(MODEL_PATH)
model = MarianMTModel.from_pretrained(MODEL_PATH)


# ============================================================
# GENERATE PREDICTIONS
# ============================================================

print()
print("=" * 70)
print("GENERATING IDIOM TRANSLATIONS")
print("=" * 70)


predictions = []

for index, row in df.iterrows():

    hindi_text = str(row["hindi_sentence"])
    expected = str(row["english_translation"])

    inputs = tokenizer(
        hindi_text,
        return_tensors="pt",
        truncation=True,
        max_length=128
    )

    translated = model.generate(
        **inputs,
        max_length=128,
        num_beams=4,
        early_stopping=True
    )

    prediction = tokenizer.decode(
        translated[0],
        skip_special_tokens=True
    )

    predictions.append(prediction)

    print(f"{index + 1}. {row['hindi_idiom']}")
    print(f"   Expected   : {expected}")
    print(f"   Prediction : {prediction}")
    print()


# ============================================================
# SAVE PREDICTIONS
# ============================================================

df["model_prediction"] = predictions

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

print("=" * 70)
print(f"Predictions saved to: {OUTPUT_PATH}")
print("=" * 70)


# ============================================================
# BLEU SCORE
# ============================================================

references = [
    [str(x).lower().split()]
    for x in df["english_translation"]
]

hypotheses = [
    str(x).lower().split()
    for x in df["model_prediction"]
]


smooth = SmoothingFunction().method1

bleu = corpus_bleu(
    references,
    hypotheses,
    smoothing_function=smooth
)


# ============================================================
# FINAL RESULT
# ============================================================

print()
print("=" * 70)
print("FINAL IDIOM-SPECIALIZED MODEL EVALUATION")
print("=" * 70)

print(f"Total examples : {len(df)}")
print(f"BLEU score     : {bleu:.6f}")
print(f"BLEU percentage: {bleu * 100:.2f}")

print("=" * 70)
print("Evaluation completed successfully.")
print("=" * 70)