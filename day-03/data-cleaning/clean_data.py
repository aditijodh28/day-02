from pathlib import Path
import pandas as pd
import numpy as np

# ---------------------------------------------------
# PATHS
# ---------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_DIR = BASE_DIR / "dataset"

INPUT_FILE = DATASET_DIR / "facility_hygiene_ml_dataset.xlsx"

CLEANED_FILE = DATASET_DIR / "cleaned_facility_dataset.csv"


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

print("=" * 60)
print("FACILITY HYGIENE DATA ANALYSIS")
print("=" * 60)

print("\nLoading dataset...")

df = pd.read_excel(INPUT_FILE)

print("Dataset loaded successfully!")


# ---------------------------------------------------
# BASIC INFORMATION
# ---------------------------------------------------

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- LAST 5 ROWS ---")
print(df.tail())

print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- DATASET INFORMATION ---")
df.info()


# ---------------------------------------------------
# MISSING VALUES
# ---------------------------------------------------

print("\n--- MISSING VALUES ---")

missing_values = df.isnull().sum()

print(missing_values)


# ---------------------------------------------------
# DUPLICATE VALUES
# ---------------------------------------------------

print("\n--- DUPLICATE ROWS ---")

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)


# ---------------------------------------------------
# STATISTICAL SUMMARY
# ---------------------------------------------------

print("\n--- STATISTICAL SUMMARY ---")

print(df.describe(include="all"))


# ---------------------------------------------------
# NUMERIC COLUMNS
# ---------------------------------------------------

numeric_columns = df.select_dtypes(
    include=np.number
).columns

print("\n--- NUMERIC COLUMNS ---")
print(numeric_columns.tolist())


# ---------------------------------------------------
# UNIQUE VALUES
# ---------------------------------------------------

print("\n--- UNIQUE VALUES ---")

for column in df.columns:
    print(
        f"{column}: {df[column].nunique()} unique values"
    )


# ---------------------------------------------------
# LOCATION VALUES
# ---------------------------------------------------

if "location" in df.columns:
    print("\n--- LOCATIONS ---")
    print(df["location"].value_counts())


print("\nInitial inspection completed.")

print("\n" + "=" * 60)
print("DATA VALIDATION")
print("=" * 60)


# ---------------------------------------------------
# CLEANLINESS SCORE VALIDATION
# ---------------------------------------------------

if "cleanliness_score" in df.columns:

    invalid_cleanliness = df[
        (df["cleanliness_score"] < 0) |
        (df["cleanliness_score"] > 100)
    ]

    print(
        "\nInvalid cleanliness scores:",
        len(invalid_cleanliness)
    )


# ---------------------------------------------------
# ODOR SCORE VALIDATION
# ---------------------------------------------------

if "odor_score" in df.columns:

    invalid_odor = df[
        (df["odor_score"] < 0) |
        (df["odor_score"] > 100)
    ]

    print(
        "Invalid odor scores:",
        len(invalid_odor)
    )


# ---------------------------------------------------
# FOOTFALL VALIDATION
# ---------------------------------------------------

if "footfall" in df.columns:

    invalid_footfall = df[
        df["footfall"] < 0
    ]

    print(
        "Invalid footfall values:",
        len(invalid_footfall)
    )


# ---------------------------------------------------
# COMPLAINT VALIDATION
# ---------------------------------------------------

if "complaints" in df.columns:

    invalid_complaints = df[
        df["complaints"] < 0
    ]

    print(
        "Invalid complaint values:",
        len(invalid_complaints)
    )

    print("\nRemoving duplicate rows...")

before_duplicates = len(df)

df = df.drop_duplicates()

after_duplicates = len(df)

print(
    "Duplicates removed:",
    before_duplicates - after_duplicates
)

numeric_columns = df.select_dtypes(
    include=np.number
).columns

for column in numeric_columns:

    if df[column].isnull().sum() > 0:

        median_value = df[column].median()

        df[column] = df[column].fillna(
            median_value
        )

        print(
            f"Filled missing values in {column} "
            f"with median {median_value}"
        )
        print("\n" + "=" * 60)
print("NUMPY ANALYSIS")
print("=" * 60)

if "cleanliness_score" in df.columns:

    scores = df[
        "cleanliness_score"
    ].to_numpy()

    print("\nArray:")
    print(scores)

    print("\nDimensions:")
    print(scores.ndim)

    print("\nShape:")
    print(scores.shape)

    print("\nFirst value:")
    print(scores[0])

    print("\nFirst five values:")
    print(scores[:5])

    print("\nTotal:")
    print(np.sum(scores))

    print("\nMean:")
    print(np.mean(scores))

    print("\nMaximum:")
    print(np.max(scores))

    print("\nMinimum:")
    print(np.min(scores))

    print("\nStandard deviation:")
    print(np.std(scores))

    df.to_csv(
    CLEANED_FILE,
    index=False
)

print("\n" + "=" * 60)
print("CLEANED DATASET SAVED")
print("=" * 60)

print(
    f"Saved to: {CLEANED_FILE}"
)

print("\nFinal shape:")
print(df.shape)

print("\nRemaining missing values:")
print(df.isnull().sum())