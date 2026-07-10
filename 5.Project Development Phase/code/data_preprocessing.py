import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def load_data(csv_path="data/hdi_data.csv"):
    return pd.read_csv(csv_path)


def select_features(df):
    X = df.iloc[:, [0, 2, 3, 4, 5]]
    y = df.iloc[:, 6]
    return X, y


def check_null_values(X):
    print("Null values in each column:")
    print(X.isnull().sum())
    return X.isnull().sum()


def fill_null_values(X):
    return X.fillna(X.mean(numeric_only=True))


def encode_country(X):
    le = LabelEncoder()
    X_encoded = X.copy()
    X_encoded["country"] = le.fit_transform(X_encoded["country"])
    return X_encoded, le


def split_data(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    print(f"Training set:   X_train {X_train.shape}, y_train {y_train.shape}")
    print(f"Testing set:    X_test  {X_test.shape}, y_test  {y_test.shape}")
    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    df = load_data()
    X, y = select_features(df)
    check_null_values(X)
    X_clean = fill_null_values(X)
    X_encoded, encoder = encode_country(X_clean)
    X_train, X_test, y_train, y_test = split_data(X_encoded, y)
