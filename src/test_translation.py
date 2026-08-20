from transformers import MarianMTModel, MarianTokenizer

model_name = "Helsinki-NLP/opus-mt-hi-en"

tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Hindi sentence for testing
hindi_text = "मुझे कृत्रिम बुद्धिमत्ता सीखना पसंद है।"

# Convert Hindi text into tokens
inputs = tokenizer(hindi_text, return_tensors="pt")

# Generate English translation
translated = model.generate(**inputs)

# Convert model output back to text
english_text = tokenizer.decode(translated[0], skip_special_tokens=True)

print("Hindi:", hindi_text)
print("English:", english_text)