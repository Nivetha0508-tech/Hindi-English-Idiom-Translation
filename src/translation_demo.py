from transformers import MarianMTModel, MarianTokenizer

MODEL_PATH = "./fine_tuned_large_model"

print("Loading fine-tuned Hindi → English model...")

tokenizer = MarianTokenizer.from_pretrained(MODEL_PATH)
model = MarianMTModel.from_pretrained(MODEL_PATH)

print("Model loaded successfully!")
print("\nHindi → English Translation Demo")
print("Type 'exit' to stop.\n")

while True:
    hindi_text = input("Enter Hindi sentence: ")

    if hindi_text.lower() == "exit":
        print("Demo ended.")
        break

    if not hindi_text.strip():
        print("Please enter a Hindi sentence.\n")
        continue

    inputs = tokenizer(
        hindi_text,
        return_tensors="pt",
        truncation=True,
        max_length=128
    )

    output = model.generate(
        **inputs,
        max_length=128
    )

    english_text = tokenizer.decode(
        output[0],
        skip_special_tokens=True
    )

    print("English:", english_text)
    print("-" * 60)