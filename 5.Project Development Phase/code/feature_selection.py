import pandas as pd

df = pd.read_csv("data/hdi_data.csv")

print("Column index mappings:")
for i, col in enumerate(df.columns):
    print(f"  Index {i}: {col}")

# Independent variables (X): selected by column index
# Index 0 -> country (categorical)
# Index 2 -> life_expectancy
# Index 3 -> expected_years_schooling
# Index 4 -> mean_years_schooling
# Index 5 -> gni_per_capita
X = df.iloc[:, [0, 2, 3, 4, 5]]

# Dependent variable (y): HDI score at index 6
y = df.iloc[:, 6]

print(f"\nIndependent Variables (X) shape: {X.shape}")
print(f"Columns: {X.columns.tolist()}")
print(f"\nDependent Variable (y) shape: {y.shape}")
print(f"Target: {y.name}")

print("\nFirst 3 rows of X:")
print(X.head(3))
print("\nFirst 3 values of y:")
print(y.head(3))
