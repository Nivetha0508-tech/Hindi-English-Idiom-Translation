import csv

search_term = "कृत्रिम बुद्धिमत्ता"

with open("data/train.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    found = 0

    for row in reader:
        if search_term in row["hindi"]:
            print("Hindi:", row["hindi"])
            print("English:", row["english"])
            print("-" * 50)
            found += 1

print("Matching pairs found:", found)