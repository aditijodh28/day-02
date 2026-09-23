from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Cleaned dataset
DATASET_FILE = BASE_DIR / "dataset" / "cleaned_facility_dataset.csv"

# Visualization folder
OUTPUT_DIR = BASE_DIR / "visualizations"

# Create visualization folder automatically
OUTPUT_DIR.mkdir(exist_ok=True)

# Read cleaned dataset
df = pd.read_csv(DATASET_FILE)

print("Dataset loaded successfully!")
print(df.head())

# -----------------------------------------
# 1. CLEANLINESS BY LOCATION
# -----------------------------------------

location_cleanliness = df.groupby(
    "location"
)["cleanliness_score"].mean()

plt.figure(figsize=(10, 6))

location_cleanliness.plot(kind="bar")

plt.title("Average Cleanliness Score by Location")
plt.xlabel("Location")
plt.ylabel("Average Cleanliness Score")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "cleanliness_by_location.png"
)

plt.close()

print("Created cleanliness_by_location.png")

# -----------------------------------------
# 2. COMPLAINTS BY LOCATION
# -----------------------------------------

location_complaints = df.groupby(
    "location"
)["complaints"].sum()

plt.figure(figsize=(10, 6))

location_complaints.plot(kind="bar")

plt.title("Total Complaints by Location")
plt.xlabel("Location")
plt.ylabel("Total Complaints")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "complaints_by_location.png"
)

plt.close()

print("Created complaints_by_location.png")

# -----------------------------------------
# 3. CLEANLINESS DISTRIBUTION
# -----------------------------------------

plt.figure(figsize=(10, 6))

plt.hist(
    df["cleanliness_score"],
    bins=10
)

plt.title("Distribution of Cleanliness Scores")
plt.xlabel("Cleanliness Score")
plt.ylabel("Number of Facilities")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "cleanliness_distribution.png"
)

plt.close()

print("Created cleanliness_distribution.png")

# -----------------------------------------
# 4. FOOTFALL VS COMPLAINTS
# -----------------------------------------

plt.figure(figsize=(10, 6))

plt.scatter(
    df["footfall"],
    df["complaints"]
)

plt.title("Footfall vs Complaints")
plt.xlabel("Footfall")
plt.ylabel("Complaints")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "footfall_vs_complaints.png"
)

plt.close()

print("Created footfall_vs_complaints.png")

# -----------------------------------------
# 5. CLEANLINESS OVER TIME
# -----------------------------------------

df["inspection_date"] = pd.to_datetime(
    df["inspection_date"],
    errors="coerce"
)

date_summary = df.groupby(
    "inspection_date"
)["cleanliness_score"].mean()

plt.figure(figsize=(12, 6))

date_summary.plot(
    kind="line",
    marker="o"
)

plt.title("Average Cleanliness Score Over Time")
plt.xlabel("Inspection Date")
plt.ylabel("Average Cleanliness Score")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "cleanliness_over_time.png"
)

plt.close()

print("Created cleanliness_over_time.png")

print("\n" + "=" * 60)
print("KEY STATISTICS")
print("=" * 60)

print(
    "\nAverage cleanliness:",
    df["cleanliness_score"].mean()
)

print(
    "Median cleanliness:",
    df["cleanliness_score"].median()
)

print(
    "Maximum cleanliness:",
    df["cleanliness_score"].max()
)

print(
    "Minimum cleanliness:",
    df["cleanliness_score"].min()
)

print(
    "\nAverage odor score:",
    df["odor_score"].mean()
)

print(
    "Average waste level:",
    df["waste_level"].mean()
)

print(
    "Average footfall:",
    df["footfall"].mean()
)

print(
    "Total complaints:",
    df["complaints"].sum()
)