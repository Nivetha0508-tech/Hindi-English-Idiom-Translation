from datasets import load_dataset
from transformers import MarianMTModel, MarianTokenizer
import sacrebleu

MODEL_PATH = "Helsinki-NLP/opus-mt-hi-en"

print("Loading original pretrained model...")

tokenizer = MarianTokenizer.from_pretrained(MODEL_PATH)
model = MarianMTModel.from_pretrained(MODEL_PATH)

print("Loading validation dataset...")

dataset = load_dataset(
    "csv",
    data_files="data/validation_large.csv"
)["train"]

print("Original validation examples:", len(dataset))

# Remove missing or empty translations
dataset = dataset.filter(
    lambda x:
        x["hindi"] is not None
        and x["english"] is not None
        and str(x["hindi"]).strip() != ""
        and str(x["english"]).strip() != ""
)

print("Valid validation examples:", len(dataset))

predictions = []
references = []

print("\nEvaluating original pretrained model...")

for i, example in enumerate(dataset):

    hindi = str(example["hindi"]).strip()
    english = str(example["english"]).strip()

    inputs = tokenizer(
        hindi,
        return_tensors="pt",
        truncation=True,
        max_length=128
    )

    output = model.generate(
        **inputs,
        max_length=128
    )

    prediction = tokenizer.decode(
        output[0],
        skip_special_tokens=True
    )

    predictions.append(prediction)
    references.append(english)

    if (i + 1) % 100 == 0:
        print(f"Evaluated: {i + 1}/{len(dataset)}")

bleu = sacrebleu.corpus_bleu(
    predictions,
    [references]
)

print("\n" + "=" * 60)
print("ORIGINAL MODEL EVALUATION COMPLETED")
print("=" * 60)
print("Original Model BLEU Score:", bleu.score)
print("Valid validation examples:", len(dataset))
print("=" * 60)