from datasets import load_dataset

dataset = load_dataset("cfilt/iitb-english-hindi", split="train[:100]")

print(dataset)
print(dataset[0])