import pandas as pd
import category_encoders as ce

# Load datetime-feature dataset
df = pd.read_csv("data/processed/bike_datetime_features.csv")

# Target variable
target = "count"

# Categorical columns
categorical_columns = [
    "season",
    "holiday",
    "workingday",
    "weather"
]

# Separate features and target
X = df.drop(columns=[target])
y = df[target]

# Create Target Encoder
encoder = ce.TargetEncoder(
    cols=categorical_columns
)

# Fit and transform
X_encoded = encoder.fit_transform(X, y)

# Add target back
X_encoded[target] = y

# Save result
X_encoded.to_csv(
    "data/processed/bike_target_encoded.csv",
    index=False
)

print("Target Encoding completed!")
print("New Shape:", X_encoded.shape)

print("\nFirst 5 Rows:")
print(X_encoded.head())