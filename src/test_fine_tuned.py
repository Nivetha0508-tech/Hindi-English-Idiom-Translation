from transformers import MarianMTModel, MarianTokenizer

model_path = "./fine_tuned_model"

print("Loading fine-tuned model...")

tokenizer = MarianTokenizer.from_pretrained(model_path)
model = MarianMTModel.from_pretrained(model_path)

# Same sentence we tested before fine-tuning
hindi_text = "मुझे कृत्रिम बुद्धिमत्ता सीखना पसंद है।"

inputs = tokenizer(
    hindi_text,
    return_tensors="pt"
)

translated = model.generate(**inputs)

english_text = tokenizer.decode(
    translated[0],
    skip_special_tokens=True
)

print("Hindi:", hindi_text)
print("English:", english_text)