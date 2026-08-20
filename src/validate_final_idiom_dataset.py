import pandas as pd

FILE_PATH = "data/verified_hindi_english_idioms.csv"

df = pd.read_csv(FILE_PATH)

print("=" * 60)
print("FINAL IDIOM DATASET QUALITY CHECK")
print("=" * 60)

# 1. Row count
print(f"\nTotal rows: {len(df)}")

# 2. Expected columns
expected_columns = [
    "id",
    "hindi_idiom",
    "hindi_sentence",
    "english_translation",
    "idiom_meaning"
]

print("\nColumn check:")
for column in expected_columns:
    if column in df.columns:
        print(f"  PASS - {column}")
    else:
        print(f"  FAIL - {column}")

# 3. Missing values
missing = df[expected_columns].isnull().sum()

print("\nMissing-value check:")
if missing.sum() == 0:
    print("  PASS - No missing values")
else:
    print("  FAIL - Missing values found")
    print(missing)

# 4. Duplicate IDs
duplicate_ids = df[df["id"].duplicated(keep=False)]

print("\nDuplicate ID check:")
if duplicate_ids.empty:
    print("  PASS - No duplicate IDs")
else:
    print("  FAIL - Duplicate IDs found")
    print(duplicate_ids["id"].tolist())

# 5. Duplicate Hindi idioms
duplicate_idioms = df[df["hindi_idiom"].duplicated(keep=False)]

print("\nDuplicate idiom check:")
if duplicate_idioms.empty:
    print("  PASS - No duplicate idioms")
else:
    print("  WARNING - Duplicate idioms found:")
    print(duplicate_idioms["hindi_idiom"].tolist())

# 6. Empty-string check
text_columns = [
    "hindi_idiom",
    "hindi_sentence",
    "english_translation",
    "idiom_meaning"
]

empty_values = []

for column in text_columns:
    for index, value in df[column].items():
        if not str(value).strip():
            empty_values.append((index + 1, column))

print("\nEmpty-text check:")
if not empty_values:
    print("  PASS - No empty text fields")
else:
    print("  FAIL - Empty fields found:")
    for item in empty_values:
        print(f"    Row {item[0]}: {item[1]}")

# 7. ID sequence check
expected_ids = list(range(1, len(df) + 1))
actual_ids = df["id"].tolist()

print("\nID sequence check:")
if actual_ids == expected_ids:
    print("  PASS - IDs are sequential from 1 to 63")
else:
    print("  WARNING - ID sequence is not sequential")

# 8. Translation length check
short_translations = df[
    df["english_translation"].astype(str).str.len() < 10
]

print("\nEnglish translation length check:")
if short_translations.empty:
    print("  PASS - No suspiciously short translations")
else:
    print("  WARNING - Very short translations:")
    for _, row in short_translations.iterrows():
        print(f"    {row['id']}: {row['english_translation']}")

# Final result
print("\n" + "=" * 60)

technical_checks = [
    len(df) == 63,
    all(column in df.columns for column in expected_columns),
    missing.sum() == 0,
    duplicate_ids.empty,
    not empty_values,
    actual_ids == expected_ids
]

if all(technical_checks):
    print("FINAL RESULT: PASS")
    print("The dataset is technically ready for model evaluation.")
else:
    print("FINAL RESULT: REVIEW REQUIRED")

print("=" * 60)