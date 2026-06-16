"""
Business Project 10 — Price vs Quantity Bubble Chart
"""

from pathlib import Path
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "a_business_data_2800.csv", parse_dates=["order_date"])
sample = df.sample(200, random_state=42)
fig = px.scatter(sample, x="price", y="quantity", size="revenue", color="product_category",
                 hover_data=["country", "marketing_channel"], title="Price vs Quantity Bubble Chart")
fig.write_image(PLOTS_DIR / "project10_price_quantity_bubble.png")
print("Saved plots/project10_price_quantity_bubble.png")
