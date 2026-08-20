from transformers import MarianMTModel, MarianTokenizer

model_path = "./fine_tuned_large_model"

print("Loading fine-tuned model...")

tokenizer = MarianTokenizer.from_pretrained(model_path)
model = MarianMTModel.from_pretrained(model_path)

test_sentences = [
    "मुझे आज बहुत खुशी हो रही है।",
    "भारत एक सुंदर देश है।",
    "मैं रोज़ नई चीज़ें सीखता हूँ।",
    "वह कल स्कूल गया था।",
    "कृपया मुझे यह किताब दें।"
]

print("\n--- Hindi → English Translation Results ---\n")

for hindi_text in test_sentences:

    inputs = tokenizer(
        hindi_text,
        return_tensors="pt"
    )

    translated = model.generate(
        **inputs,
        max_length=128
    )

    english_text = tokenizer.decode(
        translated[0],
        skip_special_tokens=True
    )

    print("Hindi:", hindi_text)
    print("English:", english_text)
    print("-" * 60)