import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction

# ============================================================
# PATHS
# ============================================================

MODEL_PATH = "fine_tuned_large_model"
DATA_PATH = "data/verified_hindi_english_idioms.csv"
OUTPUT_PATH = "data/verified_idiom_predictions.csv"

# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv(DATA_PATH)

print("=" * 70)
print("VERIFIED HINDI → ENGLISH IDIOM EVALUATION")
print("=" * 70)

print(f"\nTotal verified examples: {len(df)}")

# ============================================================
# DEVICE
# ============================================================

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(f"Device: {device}")

# ============================================================
# LOAD MODEL
# ============================================================

print("\nLoading fine-tuned model...")
print(f"Model: {MODEL_PATH}")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model.to(device)
model.eval()

print("Model loaded successfully.")

# ============================================================
# GENERATE TRANSLATIONS
# ============================================================

predictions = []

print("\nGenerating translations...")
print("=" * 70)

for index, row in df.iterrows():

    hindi_sentence = str(row["hindi_sentence"])

    inputs = tokenizer(
        hindi_sentence,
        return_tensors="pt",
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
            num_beams=4
        )

    prediction = tokenizer.decode(
        generated_ids[0],
        skip_special_tokens=True
    ).strip()

    predictions.append(prediction)

    print(f"\n{index + 1}. {row['hindi_idiom']}")
    print(f"   Hindi     : {hindi_sentence}")
    print(f"   Expected  : {row['english_translation']}")
    print(f"   Predicted : {prediction}")

# ============================================================
# SAVE PREDICTIONS
# ============================================================

df["model_prediction"] = predictions

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8-sig"
)

print("\n" + "=" * 70)
print(f"Predictions saved to: {OUTPUT_PATH}")

# ============================================================
# BLEU CALCULATION
# ============================================================

references = []
hypotheses = []

for _, row in df.iterrows():

    reference = str(row["english_translation"]).lower().split()
    hypothesis = str(row["model_prediction"]).lower().split()

    references.append([reference])
    hypotheses.append(hypothesis)

smooth = SmoothingFunction().method1

bleu_score = corpus_bleu(
    references,
    hypotheses,
    smoothing_function=smooth
)

bleu_percentage = bleu_score * 100

# ============================================================
# FINAL RESULT
# ============================================================

print("\n" + "=" * 70)
print("FINAL IDIOM EVALUATION RESULT")
print("=" * 70)

print(f"Total examples : {len(df)}")
print(f"BLEU score     : {bleu_score:.6f}")
print(f"BLEU percentage: {bleu_percentage:.2f}")

print("=" * 70)
print("Evaluation completed successfully.")
print("=" * 70)