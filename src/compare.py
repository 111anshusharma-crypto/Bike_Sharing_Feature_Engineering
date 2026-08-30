import pandas as pd

# Load One-Hot Encoded dataset
one_hot = pd.read_csv(
    "data/processed/bike_one_hot_encoded.csv"
)

# Load Target Encoded dataset
target_encoded = pd.read_csv(
    "data/processed/bike_target_encoded.csv"
)

print("========== ONE-HOT ENCODING ==========")
print("Shape:", one_hot.shape)

print("\nColumns:")
print(one_hot.columns.tolist())


print("\n========== TARGET ENCODING ==========")
print("Shape:", target_encoded.shape)

print("\nColumns:")
print(target_encoded.columns.tolist())


print("\n========== SAMPLE DATA ==========")

print("\nOne-Hot Encoding:")
print(one_hot.head())

print("\nTarget Encoding:")
print(target_encoded.head())