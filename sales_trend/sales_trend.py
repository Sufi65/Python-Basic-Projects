import pandas as pd
import matplotlib.pyplot as plt

def sales_trend():
    df = pd.read_csv("sales.csv")

    print("=== Sales Trend Analysis ===\n")
    print(df)

    highest = df.loc[df["sales"].idxmax()]
    lowest = df.loc[df["sales"].idxmin()]

    print("\nHighest Sales:", highest["month"], "-", highest["sales"])
    print("Lowest Sales:", lowest["month"], "-", lowest["sales"])

    plt.plot(df["month"], df["sales"], marker='o')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    sales_trend()