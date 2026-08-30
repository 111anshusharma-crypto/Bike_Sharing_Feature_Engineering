# Bike Sharing Feature Engineering

## Project Overview

This project focuses on datetime feature extraction and categorical encoding using the Bike Sharing Demand dataset.

## Features

### Datetime Feature Extraction

The `datetime` column was converted into:

* Year
* Month
* Day
* Hour
* Day of Week

### One-Hot Encoding

One-Hot Encoding was applied to:

* `season`
* `holiday`
* `workingday`
* `weather`

### Target Encoding

Target Encoding was applied to categorical features using `count` as the target variable.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Category Encoders

## How to Run

```bash
source venv/bin/activate
python src/check_dataset.py
python src/datetime_features.py
python src/one_hot_encoding.py
python src/target_encoding.py
python src/compare.py
```

## Output

Processed datasets are saved in:

`data/processed/`

## Learning Outcomes

This project demonstrates datetime feature extraction, One-Hot Encoding, Target Encoding, and categorical feature transformation for machine learning.
