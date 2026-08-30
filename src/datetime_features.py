import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/train.csv")

# Convert datetime column
df["datetime"] = pd.to_datetime(df["datetime"])

# Extract datetime features
df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month
df["day"] = df["datetime"].dt.day
df["hour"] = df["datetime"].dt.hour
df["day_of_week"] = df["datetime"].dt.dayofweek

# Display result
print("Datetime Features:")
print(
    df[
        [
            "datetime",
            "year",
            "month",
            "day",
            "hour",
            "day_of_week"
        ]
    ].head(10)
)

# Save processed dataset
df.to_csv(
    "data/processed/bike_datetime_features.csv",
    index=False
)

print("\nDatetime feature extraction completed!")
print("Saved to: data/processed/bike_datetime_features.csv")