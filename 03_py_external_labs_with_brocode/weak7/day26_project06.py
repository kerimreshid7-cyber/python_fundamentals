   

# Hello how are you
# I am gonna build real analysis project per day on real data set to just practice what i have learned.


"""
Business Project 6 — Returns by Marketing Channel
"""

from pathlib import Path
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(BASE_DIR / "a_business_data_2800.csv", parse_dates=["order_date"])
returned = df.groupby("marketing_channel")["returned"].sum().reset_index()
fig = px.bar(returned, x="marketing_channel", y="returned", text="returned", color="marketing_channel",
             title="Returned Order Count by Marketing Channel")
fig.update_layout(showlegend=False)
fig.write_image(PLOTS_DIR / "project06_returns_by_channel.png")
print("Saved plots/project06_returns_by_channel.png")

# Insights:
# 1. The "Email" channel has the highest number of returned orders, indicating potential issues with customer satisfaction or product quality for customers acquired through email marketing.
# 2. The "Social Media" channel has the second-highest returns, suggesting that customers acquired through social media may also