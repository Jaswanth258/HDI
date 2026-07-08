import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pickle
import os

from data_preprocessing import load_data, select_features, fill_null_values, encode_country, split_data


def train_and_evaluate():
    df = load_data()
    X, y = select_features(df)
    X_clean = fill_null_values(X)
    X_encoded, encoder = encode_country(X_clean)
    X_train, X_test, y_train, y_test = split_data(X_encoded, y)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("\n--- y_test (Actual HDI) ---")
    print(np.array(y_test))

    print("\n--- y_pred (Predicted HDI) ---")
    print(y_pred)

    print("\n--- Comparison (first 10) ---")
    print("Actual    Predicted")
    for i in range(10):
        print(f"{y_test.values[i]:.4f}    {y_pred[i]:.4f}")

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print(f"\n--- Metrics ---")
    print(f"RMSE:        {rmse:.4f}")
    print(f"R-squared:   {r2:.4f}")
    print(f"Intercept:   {model.intercept_:.4f}")
    for col, coef in zip(X_encoded.columns, model.coef_):
        print(f"  {col}: {coef:.4f}")

    print("\n--- Test with Single Input ---")
    sample = X_test.iloc[:1]
    single_pred = model.predict(sample)[0]
    print(f"Input features: {dict(sample.iloc[0])}")
    print(f"Predicted HDI:  {single_pred:.4f}")
    print(f"Actual HDI:     {y_test.values[0]:.4f}")

    os.makedirs("models", exist_ok=True)
    with open("models/hdi_model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("\nModel saved to models/hdi_model.pkl")

    return model, X_test, y_test, y_pred


if __name__ == "__main__":
    model, X_test, y_test, y_pred = train_and_evaluate()
