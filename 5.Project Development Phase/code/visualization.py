import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os


def plot_hdi_distribution(df, save_path="static/hdi_distribution.png"):
    plt.figure(figsize=(8, 5))
    sns.histplot(df["hdi_index"], bins=20, kde=True)
    plt.title("HDI Index Distribution")
    plt.xlabel("HDI Index")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def plot_feature_correlations(df, save_path="static/correlation_heatmap.png"):
    plt.figure(figsize=(8, 6))
    corr = df[["life_expectancy", "expected_years_schooling",
               "mean_years_schooling", "gni_per_capita", "hdi_index"]].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Feature Correlations")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def plot_actual_vs_predicted(y_test, y_pred, save_path="static/actual_vs_predicted.png"):
    plt.figure(figsize=(7, 7))
    plt.scatter(y_test, y_pred, alpha=0.6)
    plt.plot([y_test.min(), y_test.max()],
             [y_test.min(), y_test.max()], "r--")
    plt.xlabel("Actual HDI")
    plt.ylabel("Predicted HDI")
    plt.title("Actual vs Predicted HDI")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    df = pd.read_csv("data/hdi_data.csv")
    plot_hdi_distribution(df)
    plot_feature_correlations(df)
    print("Visualizations saved to static/")
