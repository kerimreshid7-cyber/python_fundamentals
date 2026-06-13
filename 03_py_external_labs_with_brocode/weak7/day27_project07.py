

# hello how are you today 
# I am gonna do mini anlytics project on the business data. to understand monthly revenue trend.


"""
Business Project 7 — Monthly Revenue Trend
"""

from pathlib import Path
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "a_business_data_2800.csv", parse_dates=["order_date"])
monthly = df.set_index("order_date").resample("ME")["revenue"].sum().reset_index()
fig = px.line(monthly, x="order_date", y="revenue", markers=True, title="Monthly Revenue Trend")
fig.update_xaxes(title="Month")
fig.update_yaxes(title="Revenue")
fig.write_image(PLOTS_DIR / "project07_monthly_revenue_trend.png")
print("Saved plots/project07_monthly_revenue_trend.png")
