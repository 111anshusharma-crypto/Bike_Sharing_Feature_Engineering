# Bike Sharing Feature Engineering

## Project Overview

This project practices datetime feature extraction and categorical encoding using the Bike Sharing Demand dataset.

The main objective is to transform raw datetime and categorical data into machine-learning-ready features.

## Dataset

**Dataset:** Bike Sharing Demand

The dataset contains bike rental information along with datetime, weather, temperature, humidity, and other features.

## Feature Engineering

### 1. Datetime Feature Extraction

The `datetime` column was converted into separate features:

* Year
* Month
* Day
* Hour
* Day of Week

### 2. One-Hot Encoding

Categorical columns were encoded using One-Hot Encoding:

* `season`
* `holiday`
* `workingday`
* `weather`

### 3. Target Encoding

Target Encoding was also applied to the categorical columns using `count` as the target variable.

## Project Structure

```text
Bike_Sharing_Feature_Engineering/
│
├── data/
│   ├── raw/
│   │   └── train.csv
│   │
│   └── processed/
│       ├── bike_datetime_features.csv
│       ├── bike_one_hot_encoded.csv
│       └── bike_target_encoded.csv
│
├── src/
│   ├── check_dataset.py
│   ├── datetime_features.py
│   ├── one_hot_encoding.py
│   ├── target_encoding.py
│   └── compare.py
│
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Category Encoders

## How to Run

Activate the virtual environment:

```bash
source venv/bin/activate
```

Check the dataset:

```bash
python src/check_dataset.py
```

Extract datetime features:

```bash
python src/datetime_features.py
```

Apply One-Hot Encoding:

```bash
python src/one_hot_encoding.py
```

Apply Target Encoding:

```bash
python src/target_encoding.py
```

Compare the encoded datasets:

```bash
python src/compare.py
```

## Output

The processed datasets are saved inside:

```text
data/processed/
```

### Learning Outcome

This project demonstrates how raw datetime and categorical features can be transformed into useful numerical features for machine learning.
