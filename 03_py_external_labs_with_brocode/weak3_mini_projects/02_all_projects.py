"""
25 Mini Projects: Business + Football Visual Analysis
Uses matplotlib, seaborn, and plotly for 25 distinct visual mini projects.
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
PLOTS_DIR = BASE_DIR / "plots"
PLOTS_DIR.mkdir(exist_ok=True)


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    business = pd.read_csv(BASE_DIR / "a_business_data_2800.csv", parse_dates=["order_date"])
    football = pd.read_csv(BASE_DIR / "b_football_data_1300.csv", parse_dates=["date"])
    return business, football


def save_matplotlib_figure(name: str) -> None:
    path = PLOTS_DIR / f"{name}.png"
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Saved: {path}")


def save_plotly_figure(fig, name: str) -> None:
    html_path = PLOTS_DIR / f"{name}.html"
    fig.write_html(html_path, include_plotlyjs='cdn')
    print(f"Saved interactive: {html_path}")


# Business dataset projects

def project_1_revenue_by_category(df_business: pd.DataFrame) -> None:
    revenue_by_cat = df_business.groupby("product_category")["revenue"].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    revenue_by_cat.plot(kind="bar", color="#4c72b0")
    plt.title("Revenue by Product Category")
    plt.ylabel("Total Revenue")
    plt.xlabel("Product Category")
    save_matplotlib_figure("project_01_revenue_by_category")


def project_2_orders_by_country(df_business: pd.DataFrame) -> None:
    orders_country = df_business["country"].value_counts().head(10)
    plt.figure(figsize=(8, 8))
    orders_country.plot(kind="pie", autopct="%1.1f%%", startangle=140, pctdistance=0.75)
    plt.title("Top 10 Countries by Order Count")
    plt.ylabel("")
    save_matplotlib_figure("project_02_orders_by_country")


def project_3_price_distribution(df_business: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    sns.histplot(df_business["price"], kde=True, color="#2ca02c", bins=35)
    plt.title("Product Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Count")
    save_matplotlib_figure("project_03_price_distribution")


def project_4_quantity_vs_revenue(df_business: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    sns.regplot(data=df_business, x="quantity", y="revenue", scatter_kws={"alpha": 0.4})
    plt.title("Quantity vs Revenue")
    plt.xlabel("Quantity")
    plt.ylabel("Revenue")
    save_matplotlib_figure("project_04_quantity_vs_revenue")


def project_5_delivery_days_boxplot(df_business: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="delivery_days", data=df_business, color="#ff7f0e")
    plt.title("Delivery Days Distribution")
    plt.xlabel("Delivery Days")
    save_matplotlib_figure("project_05_delivery_days_boxplot")


def project_6_returns_by_channel(df_business: pd.DataFrame) -> None:
    returned = df_business.groupby("marketing_channel")["returned"].sum().reset_index()
    fig = px.bar(returned, x="marketing_channel", y="returned", text="returned", color="marketing_channel",
                 title="Returned Order Count by Marketing Channel")
    fig.update_layout(showlegend=False)
    save_plotly_figure(fig, "project_06_returns_by_channel")


def project_7_monthly_revenue_trend(df_business: pd.DataFrame) -> None:
    df_month = df_business.set_index("order_date").resample("M")["revenue"].sum().reset_index()
    fig = px.line(df_month, x="order_date", y="revenue", title="Monthly Revenue Trend", markers=True)
    fig.update_xaxes(title="Month")
    fig.update_yaxes(title="Revenue")
    save_plotly_figure(fig, "project_07_monthly_revenue_trend")


def project_8_top_customers_by_revenue(df_business: pd.DataFrame) -> None:
    top_customers = df_business.groupby("customer_id")["revenue"].sum().nlargest(10)
    plt.figure(figsize=(10, 6))
    top_customers.plot(kind="barh", color="#9467bd")
    plt.title("Top 10 Customers by Revenue")
    plt.xlabel("Revenue")
    plt.gca().invert_yaxis()
    save_matplotlib_figure("project_08_top_customers_by_revenue")


def project_9_category_revenue_share(df_business: pd.DataFrame) -> None:
    category_share = df_business.groupby("product_category")["revenue"].sum().reset_index()
    fig = px.pie(category_share, names="product_category", values="revenue", hole=0.35,
                 title="Revenue Share by Product Category")
    save_plotly_figure(fig, "project_09_category_revenue_share")


def project_10_price_quantity_bubble(df_business: pd.DataFrame) -> None:
    sample = df_business.sample(200, random_state=42)
    fig = px.scatter(sample, x="price", y="quantity", size="revenue", color="product_category",
                     hover_data=["country", "marketing_channel"], title="Price vs Quantity Bubble Chart")
    save_plotly_figure(fig, "project_10_price_quantity_bubble")


def project_11_daily_order_count(df_business: pd.DataFrame) -> None:
    daily = df_business.groupby(df_business["order_date"].dt.date).size().reset_index(name="orders")
    plt.figure(figsize=(12, 5))
    sns.lineplot(data=daily, x="order_date", y="orders", marker="o")
    plt.title("Daily Order Count")
    plt.xlabel("Date")
    plt.ylabel("Number of Orders")
    plt.xticks(rotation=45)
    save_matplotlib_figure("project_11_daily_order_count")


def project_12_country_revenue_heatmap(df_business: pd.DataFrame) -> None:
    pivot = df_business.pivot_table(index="country", columns="marketing_channel", values="revenue", aggfunc="sum", fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot, annot=False, cmap="Blues", linewidths=0.5)
    plt.title("Revenue by Country and Marketing Channel")
    plt.xlabel("Marketing Channel")
    plt.ylabel("Country")
    save_matplotlib_figure("project_12_country_revenue_heatmap")


def project_13_goals_by_team(df_football: pd.DataFrame) -> None:
    goals_team = df_football.groupby("team")["goals"].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    goals_team.plot(kind="bar", color="#d62728")
    plt.title("Top 10 Teams by Total Goals")
    plt.ylabel("Goals")
    plt.xlabel("Team")
    save_matplotlib_figure("project_13_goals_by_team")


def project_14_top_assist_players(df_football: pd.DataFrame) -> None:
    assists_player = df_football.groupby("player")["assists"].sum().nlargest(12)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=assists_player.values, y=assists_player.index, palette="viridis")
    plt.title("Top Assist Players")
    plt.xlabel("Assists")
    plt.ylabel("Player")
    save_matplotlib_figure("project_14_top_assist_players")


def project_15_shots_vs_passes(df_football: pd.DataFrame) -> None:
    fig = px.scatter(df_football, x="shots", y="passes", color="result", size="minutes_played",
                     hover_data=["player", "team", "opponent"], title="Shots vs Passes by Match Result")
    save_plotly_figure(fig, "project_15_shots_vs_passes")


def project_16_minutes_played_violin(df_football: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    sns.violinplot(x="result", y="minutes_played", data=df_football, palette="pastel")
    plt.title("Minutes Played by Match Result")
    plt.xlabel("Result")
    plt.ylabel("Minutes Played")
    save_matplotlib_figure("project_16_minutes_played_violin")


def project_17_goals_per_match_trend(df_football: pd.DataFrame) -> None:
    team_goals = df_football.groupby(["date", "team"]).sum().reset_index()
    fig = px.line(team_goals, x="date", y="goals", color="team", title="Goals per Match Trend by Team", line_shape="spline")
    fig.update_layout(showlegend=False)
    save_plotly_figure(fig, "project_17_goals_per_match_trend")


def project_18_player_contribution_ratio(df_football: pd.DataFrame) -> None:
    ratio = df_football.groupby("player")["goals", "assists"].sum()
    ratio = ratio[ratio.sum(axis=1) > 0]
    ratio["contribution"] = ratio["goals"] + ratio["assists"]
    top = ratio.sort_values("contribution", ascending=False).head(15)
    plt.figure(figsize=(10, 7))
    sns.barplot(x=top["contribution"], y=top.index, palette="magma")
    plt.title("Top Player Contribution (Goals + Assists)")
    plt.xlabel("Contribution")
    plt.ylabel("Player")
    save_matplotlib_figure("project_18_player_contribution_ratio")


def project_19_result_distribution(df_football: pd.DataFrame) -> None:
    result_counts = df_football["result"].value_counts()
    fig = px.pie(result_counts, names=result_counts.index, values=result_counts.values, hole=0.4,
                 title="Match Result Distribution")
    save_plotly_figure(fig, "project_19_result_distribution")


def project_20_top_performers_scatter(df_football: pd.DataFrame) -> None:
    summary = df_football.groupby("player")["goals", "assists", "minutes_played"].sum()
    summary = summary[summary["minutes_played"] > 50]
    summary["total_contribution"] = summary["goals"] + summary["assists"]
    fig = px.scatter(summary.reset_index(), x="minutes_played", y="total_contribution", color="goals",
                     size="goals", hover_data=["player", "assists"], title="Top Performers: Contribution vs Minutes")
    save_plotly_figure(fig, "project_20_top_performers_scatter")


def project_21_passes_boxplot_by_result(df_football: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="result", y="passes", data=df_football, palette="Set2")
    plt.title("Passes by Match Result")
    plt.xlabel("Result")
    plt.ylabel("Passes")
    save_matplotlib_figure("project_21_passes_boxplot_by_result")


def project_22_team_performance_heatmap(df_football: pd.DataFrame) -> None:
    pivot = df_football.pivot_table(index="team", columns="result", values="goals", aggfunc="sum", fill_value=0)
    plt.figure(figsize=(12, 10))
    sns.heatmap(pivot, annot=True, fmt="d", cmap="rocket")
    plt.title("Goals by Team and Match Result")
    plt.xlabel("Result")
    plt.ylabel("Team")
    save_matplotlib_figure("project_22_team_performance_heatmap")


def project_23_opponent_shots_trend(df_football: pd.DataFrame) -> None:
    opponent_shots = df_football.groupby(["date", "opponent"])['shots'].sum().reset_index()
    sample = opponent_shots.sort_values('date').groupby('opponent').tail(20)
    fig = px.line(sample, x="date", y="shots", color="opponent", title="Opponent Shots Trend")
    save_plotly_figure(fig, "project_23_opponent_shots_trend")


def project_24_team_result_stacked(df_football: pd.DataFrame) -> None:
    result_team = df_football.groupby(["team", "result"]).size().reset_index(name="count")
    fig = px.bar(result_team, x="team", y="count", color="result", title="Match Result Counts by Team")
    save_plotly_figure(fig, "project_24_team_result_stacked")


def project_25_numeric_correlation_heatmap(df_football: pd.DataFrame) -> None:
    numeric = df_football[["goals", "assists", "shots", "passes", "minutes_played"]]
    corr = numeric.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title("Correlation Matrix for Football Stats")
    save_matplotlib_figure("project_25_numeric_correlation_heatmap")


def run_all_projects(save_figures: bool = True) -> None:
    business, football = load_data()
    print("Loaded datasets:", business.shape, football.shape)
    project_1_revenue_by_category(business)
    project_2_orders_by_country(business)
    project_3_price_distribution(business)
    project_4_quantity_vs_revenue(business)
    project_5_delivery_days_boxplot(business)
    project_6_returns_by_channel(business)
    project_7_monthly_revenue_trend(business)
    project_8_top_customers_by_revenue(business)
    project_9_category_revenue_share(business)
    project_10_price_quantity_bubble(business)
    project_11_daily_order_count(business)
    project_12_country_revenue_heatmap(business)
    project_13_goals_by_team(football)
    project_14_top_assist_players(football)
    project_15_shots_vs_passes(football)
    project_16_minutes_played_violin(football)
    project_17_goals_per_match_trend(football)
    project_18_player_contribution_ratio(football)
    project_19_result_distribution(football)
    project_20_top_performers_scatter(football)
    project_21_passes_boxplot_by_result(football)
    project_22_team_performance_heatmap(football)
    project_23_opponent_shots_trend(football)
    project_24_team_result_stacked(football)
    project_25_numeric_correlation_heatmap(football)
    print("Completed 25 mini projects. Plots are saved in:", PLOTS_DIR)


if __name__ == "__main__":
    run_all_projects()
