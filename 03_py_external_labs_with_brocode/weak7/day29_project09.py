"""
Business Project 9 — Category Revenue Share
"""

from pathlib import Path
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "a_business_data_2800.csv", parse_dates=["order_date"])
category_share = df.groupby("product_category")["revenue"].sum().reset_index()
fig = px.pie(category_share, names="product_category", values="revenue", hole=0.35,
             title="Revenue Share by Product Category")
fig.write_image(PLOTS_DIR / "project09_category_revenue_share.png")
print("Saved plots/project09_category_revenue_share.png")
