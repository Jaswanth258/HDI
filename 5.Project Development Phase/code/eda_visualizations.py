import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("whitegrid")
os.makedirs("static/images", exist_ok=True)

df = pd.read_csv("data/hdi_data.csv")
data1 = df.head(20)

print("=" * 50)
print("1. Unique Country Values")
print("=" * 50)
unique_countries = df["country"].unique()
print(f"Number of unique countries: {len(unique_countries)}")
print(f"Countries: {list(unique_countries)}")

print("\n" + "=" * 50)
print("2. Mean Years of Schooling vs HDI (Strip Plot)")
print("=" * 50)
plt.figure(figsize=(10, 5))
sns.stripplot(x="mean_years_schooling", y="hdi_index", data=data1,
              jitter=True, size=8, color="teal")
plt.title("Mean Years of Schooling vs HDI (First 20 Rows)")
plt.tight_layout()
plt.savefig("static/images/strip_mean_schooling_vs_hdi.png")
plt.close()
print("Saved: static/images/strip_mean_schooling_vs_hdi.png")

print("\n" + "=" * 50)
print("3. Life Expectancy vs HDI (Strip Plot)")
print("=" * 50)
plt.figure(figsize=(10, 5))
sns.stripplot(x="life_expectancy", y="hdi_index", data=data1,
              jitter=True, size=8, color="darkorange")
plt.title("Life Expectancy vs HDI (First 20 Rows)")
plt.tight_layout()
plt.savefig("static/images/strip_life_expectancy_vs_hdi.png")
plt.close()
print("Saved: static/images/strip_life_expectancy_vs_hdi.png")

print("\n" + "=" * 50)
print("4. Correlation Heatmap")
print("=" * 50)
numeric_cols = ["life_expectancy", "expected_years_schooling",
                "mean_years_schooling", "gni_per_capita", "hdi_index"]
corr = df[numeric_cols].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f",
            square=True, linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.savefig("static/images/correlation_heatmap.png")
plt.close()
print("Saved: static/images/correlation_heatmap.png")

print("\n--- Top features correlated with HDI ---")
hdi_corr = corr["hdi_index"].drop("hdi_index").sort_values(ascending=False)
for feat, val in hdi_corr.items():
    print(f"  {feat}: {val:.4f}")

print("\nAll visualizations complete.")
