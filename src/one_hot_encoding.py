import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Load datetime-feature dataset
df = pd.read_csv("data/processed/bike_datetime_features.csv")

# Categorical columns
categorical_columns = [
    "season",
    "holiday",
    "workingday",
    "weather"
]

# Create One-Hot Encoder
encoder = OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)

# Encode categorical columns
encoded = encoder.fit_transform(df[categorical_columns])

# Convert encoded data into DataFrame
encoded_df = pd.DataFrame(
    encoded,
    columns=encoder.get_feature_names_out(categorical_columns)
)

# Remove original categorical columns
df = df.drop(columns=categorical_columns)

# Combine original data with encoded data
df = pd.concat(
    [
        df.reset_index(drop=True),
        encoded_df.reset_index(drop=True)
    ],
    axis=1
)

# Save processed dataset
df.to_csv(
    "data/processed/bike_one_hot_encoded.csv",
    index=False
)

print("One-Hot Encoding completed!")
print("New Shape:", df.shape)

print("\nEncoded Columns:")
print(encoded_df.columns.tolist())
