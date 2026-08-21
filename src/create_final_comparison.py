import pandas as pd


# ============================================================
# FINAL PRE vs POST FINE-TUNING COMPARISON
# ============================================================

OUTPUT_FILE = "data/final_model_comparison.csv"


# ============================================================
# RESULTS FROM ACTUAL EVALUATIONS
# ============================================================

comparison = [
    {
        "metric": "BLEU",
        "before_idiom_finetuning": 7.85,
        "after_idiom_finetuning": 14.16,
        "unit": "score"
    },
    {
        "metric": "Average Word Overlap",
        "before_idiom_finetuning": 37.59,
        "after_idiom_finetuning": 42.46,
        "unit": "percent"
    },
    {
        "metric": "Exact Matches",
        "before_idiom_finetuning": 0,
        "after_idiom_finetuning": 1,
        "unit": "examples"
    },
    {
        "metric": "METEOR",
        "before_idiom_finetuning": None,
        "after_idiom_finetuning": 32.43,
        "unit": "percent"
    }
]


# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(comparison)


# ============================================================
# CALCULATE IMPROVEMENT
# ============================================================

df["improvement"] = (
    df["after_idiom_finetuning"]
    - df["before_idiom_finetuning"]
)


# ============================================================
# SAVE
# ============================================================

df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig"
)


# ============================================================
# DISPLAY
# ============================================================

print("=" * 75)
print("FINAL PRE vs POST IDIOM FINE-TUNING COMPARISON")
print("=" * 75)

print()

for _, row in df.iterrows():

    print(f"Metric: {row['metric']}")

    print(
        f"Before idiom fine-tuning: "
        f"{row['before_idiom_finetuning']}"
    )

    print(
        f"After idiom fine-tuning : "
        f"{row['after_idiom_finetuning']}"
    )

    if pd.notna(row["improvement"]):

        print(
            f"Improvement             : "
            f"{row['improvement']:.2f}"
        )

    else:

        print(
            "Improvement             : "
            "Not available"
        )

    print("-" * 75)


print()
print(f"Comparison saved to: {OUTPUT_FILE}")
print("=" * 75)