import json
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

file_name = Path(__file__).resolve().parent / "expenses.json"

try:
    with open(file_name, "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])

category_totals = df.groupby("category")["amount"].sum().sort_values(ascending=False)

# Historical expenses logged before the "date" field existed have no timestamp,
# and any trend shown here with only a few months of real data reflects the
# pipeline working correctly, not yet a trustworthy real spending pattern.
monthly_totals = df.groupby(df["date"].dt.to_period("M"))["amount"].sum()

category_totals.plot(kind="bar")
plt.title("Total Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount (£)")
plt.savefig("category_spending.png")
plt.show()

monthly_totals.plot(kind="line", marker="o")
plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount (£)")
plt.savefig("monthly_trend.png")
plt.show()