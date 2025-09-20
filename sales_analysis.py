"""
Sales Data Analysis Script
---------------------------
This script demonstrates:
1. Data loading & exploration
2. Basic data analysis
3. Visualizations (line, bar, histogram, scatter)
4. Findings & observations

Dataset: sales_data.csv
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    print("=== Sales Data Analysis Tool ===\n")

    try:
        # -------------------------------
        # Task 1: Load and Explore Dataset
        # -------------------------------
        print("Loading dataset...\n")

        df = pd.read_csv("sales_data.csv", parse_dates=["Date"])

        print("First 5 rows of the dataset:")
        print(df.head(), "\n")

        print("Data types and non-null counts:")
        print(df.info(), "\n")

        print("Checking for missing values:")
        print(df.isnull().sum(), "\n")

        # Clean data (fill missing with 0 just in case)
        df = df.fillna(0)

        # -------------------------------
        # Task 2: Basic Data Analysis
        # -------------------------------
        print("Basic statistics of numerical columns:")
        print(df.describe(), "\n")

        print("Average sales grouped by region:")
        grouped = df.groupby("Region")["Sales"].mean()
        print(grouped, "\n")

        # Example finding
        print("Observation: The West region tends to have the highest average sales.\n")

        # -------------------------------
        # Task 3: Visualizations
        # -------------------------------

        sns.set(style="whitegrid")

        # 1. Line chart - Sales trend over time
        plt.figure(figsize=(10, 6))
        plt.plot(df["Date"], df["Sales"], marker="o", label="Sales")
        plt.title("Line Chart: Sales Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Sales")
        plt.legend()
        plt.show()

        # 2. Bar chart - Average sales per region
        plt.figure(figsize=(8, 5))
        sns.barplot(data=df, x="Region", y="Sales", estimator="mean", ci=None)
        plt.title("Bar Chart: Average Sales by Region")
        plt.xlabel("Region")
        plt.ylabel("Average Sales")
        plt.show()

        # 3. Histogram - Distribution of Profit
        plt.figure(figsize=(8, 5))
        plt.hist(df["Profit"], bins=10, color="skyblue", edgecolor="black")
        plt.title("Histogram: Profit Distribution")
        plt.xlabel("Profit")
        plt.ylabel("Frequency")
        plt.show()

        # 4. Scatter plot - Sales vs Profit
        plt.figure(figsize=(8, 5))
        sns.scatterplot(data=df, x="Sales", y="Profit", hue="Region", style="Region")
        plt.title("Scatter Plot: Sales vs Profit by Region")
        plt.xlabel("Sales")
        plt.ylabel("Profit")
        plt.legend(title="Region")
        plt.show()

        print("✅ Analysis complete! Visualizations displayed.")

    except FileNotFoundError:
        print("✗ Error: sales_data.csv not found. Please make sure the file exists.")
    except Exception as e:
        print(f"✗ An error occurred: {e}")


if __name__ == "__main__":
    main()
