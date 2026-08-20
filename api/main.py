from fastapi import FastAPI
from pydantic import BaseModel
from transformers import MarianMTModel, MarianTokenizer
import torch


# ============================================================
# CONFIGURATION
# ============================================================

MODEL_PATH = "fine_tuned_idiom_model"


# ============================================================
# CREATE FASTAPI APP
# ============================================================

app = FastAPI(
    title="Hindi to English Idiom Translation API",
    description=(
        "Hindi to English translation API using a "
        "fine-tuned MarianMT model specialized for Hindi idioms."
    ),
    version="1.0.0"
)


# ============================================================
# REQUEST MODEL
# ============================================================

class TranslationRequest(BaseModel):
    text: str


# ============================================================
# LOAD MODEL
# ============================================================

print("=" * 70)
print("LOADING HINDI-ENGLISH IDIOM TRANSLATION MODEL")
print("=" * 70)

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

print(f"Device: {device}")
print(f"Model path: {MODEL_PATH}")

tokenizer = MarianTokenizer.from_pretrained(
    MODEL_PATH
)

model = MarianMTModel.from_pretrained(
    MODEL_PATH
)

model.to(device)
model.eval()

print("Model loaded successfully.")


# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
def root():

    return {
        "message": "Hindi to English Idiom Translation API",
        "status": "running",
        "model": MODEL_PATH
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model_loaded": True,
        "device": str(device)
    }


# ============================================================
# TRANSLATION ENDPOINT
# ============================================================

@app.post("/translate")
def translate(request: TranslationRequest):

    text = request.text.strip()

    if not text:
        return {
            "error": "Text cannot be empty."
        }

    # Tokenize input
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=128
    )

    # Move tensors to CPU/GPU
    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    # Generate translation
    with torch.no_grad():

        generated_ids = model.generate(
            **inputs,
            max_length=128,
            num_beams=4,
            early_stopping=True
        )

    # Convert generated tokens to text
    translation = tokenizer.decode(
        generated_ids[0],
        skip_special_tokens=True
    )

    return {
        "source_language": "Hindi",
        "target_language": "English",
        "input": text,
        "translation": translation
    }