from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-hi-en"

print("Loading tokenizer...")
tokenizer = MarianTokenizer.from_pretrained(model_name)

print("Loading model...")
model = MarianMTModel.from_pretrained(model_name)

print("Model loaded successfully!")