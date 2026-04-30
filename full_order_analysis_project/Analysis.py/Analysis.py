
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "orders.csv"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "analysis_charts"
OUTPUT_IMAGE = Path(__file__).resolve().parent.parent / "orders_analysis_dashboard.png"


def load_orders(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, index_col="id")
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["shipping_date"] = pd.to_datetime(df["shipping_date"], errors="coerce")
    df["discount"] = df["discount"].fillna(0.0)
    df["payment_method"] = df["payment_method"].fillna("Unknown")
    df["total_value"] = (df["price"] * df["quantity"]) - df["discount"]
    df["gross_value"] = df["price"] * df["quantity"]
    df["shipping_delay_days"] = (df["shipping_date"] - df["order_date"]).dt.days
    df["order_month"] = df["order_date"].dt.to_period("M")
    return df


def print_section(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def save_chart(fig, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=250, bbox_inches="tight")
    plt.close(fig)


def save_dashboard(df: pd.DataFrame, output_path: Path) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1) Revenue by Category
    fig, ax = plt.subplots(figsize=(10, 6))
    sales_by_category = df.groupby("category")["total_value"].sum().sort_values(ascending=False)
    sales_by_category.plot(kind="bar", ax=ax, color=["#2C7BB6", "#ABD9E9", "#FEE08B"])
    ax.set_title("Revenue by Category")
    ax.set_xlabel("")
    ax.set_ylabel("Net Sales ($)")
    save_chart(fig, OUTPUT_DIR / "01_revenue_by_category.png")

    # 2) Sales by Payment Method
    fig, ax = plt.subplots(figsize=(10, 6))
    payment_share = df.groupby("payment_method")["total_value"].sum().sort_values()
    payment_share.plot(kind="barh", ax=ax, color="#F46D43")
    ax.set_title("Sales by Payment Method")
    ax.set_xlabel("Net Sales ($)")
    save_chart(fig, OUTPUT_DIR / "02_sales_by_payment_method.png")

    # 3) Top Products by Net Revenue
    fig, ax = plt.subplots(figsize=(10, 6))
    top_products = df.groupby("product")["total_value"].sum().sort_values(ascending=False).head(8)
    top_products.plot(kind="bar", ax=ax, color="#5E4FA2")
    ax.set_title("Top 8 Products by Net Revenue")
    ax.set_xlabel("")
    ax.set_ylabel("Net Revenue ($)")
    save_chart(fig, OUTPUT_DIR / "03_top_products.png")

    # 4) Monthly Sales Trend
    fig, ax = plt.subplots(figsize=(10, 6))
    monthly_sales = df.groupby("order_month")["total_value"].sum()
    monthly_sales.plot(kind="line", ax=ax, marker="o", linewidth=2, color="#D73027")
    ax.set_title("Monthly Sales Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Net Sales ($)")
    save_chart(fig, OUTPUT_DIR / "04_monthly_sales_trend.png")

    # 5) Average Order Value by Discount Status
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_by_discount = df.groupby(df["discount"] > 0)["total_value"].mean()
    avg_by_discount.index = ["No Discount", "With Discount"]
    avg_by_discount.plot(kind="bar", ax=ax, color=["#66C2A5", "#FC8D62"])
    ax.set_title("Average Order Value by Discount Status")
    ax.set_ylabel("Average Order Value ($)")
    save_chart(fig, OUTPUT_DIR / "05_discount_impact.png")

    # 6) Order Quantity Distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df["quantity"], bins=12, kde=False, color="#8DA0CB", ax=ax)
    ax.set_title("Order Quantity Distribution")
    ax.set_xlabel("Quantity")
    ax.set_ylabel("Order Count")
    save_chart(fig, OUTPUT_DIR / "06_order_quantity_distribution.png")

    # 7) Shipping Delay Distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    delay_data = df["shipping_delay_days"].dropna()
    sns.boxplot(x=delay_data, color="#E78AC3", ax=ax)
    ax.set_title("Shipping Delay Distribution (days)")
    ax.set_xlabel("Delay Days")
    save_chart(fig, OUTPUT_DIR / "07_shipping_delay_distribution.png")

    # 8) Order Value Distribution
    fig, ax = plt.subplots(figsize=(10, 6))
    order_value = df["total_value"].dropna()
    sns.histplot(order_value, bins=20, kde=True, color="#66C2A5", ax=ax)
    ax.set_title("Order Value Distribution")
    ax.set_xlabel("Order Value ($)")
    ax.set_ylabel("Order Count")
    save_chart(fig, OUTPUT_DIR / "08_order_value_distribution.png")

    # 9) Category vs. Month Net Sales Heatmap
    fig, ax = plt.subplots(figsize=(12, 8))
    category_month = df.pivot_table(
        values="total_value",
        index="category",
        columns="order_month",
        aggfunc="sum",
        fill_value=0,
    )
    sns.heatmap(
        category_month,
        annot=True,
        fmt=".0f",
        cmap="YlGnBu",
        ax=ax,
        cbar_kws={"label": "Net Sales ($)"},
    )
    ax.set_title("Category vs. Month Net Sales")
    ax.set_xlabel("Month")
    ax.set_ylabel("Category")
    save_chart(fig, OUTPUT_DIR / "09_category_month_heatmap.png")

    # Save combined dashboard too
    fig, axes = plt.subplots(3, 3, figsize=(20, 16))
    axes = axes.flatten()
    sales_by_category.plot(kind="bar", ax=axes[0], color=["#2C7BB6", "#ABD9E9", "#FEE08B"])
    axes[0].set_title("Revenue by Category")
    axes[0].set_xlabel("")
    axes[0].set_ylabel("Net Sales ($)")
    payment_share.plot(kind="barh", ax=axes[1], color="#F46D43")
    axes[1].set_title("Sales by Payment Method")
    axes[1].set_xlabel("Net Sales ($)")
    top_products.plot(kind="bar", ax=axes[2], color="#5E4FA2")
    axes[2].set_title("Top 8 Products by Net Revenue")
    axes[2].set_xlabel("")
    axes[2].set_ylabel("Net Revenue ($)")
    monthly_sales.plot(kind="line", ax=axes[3], marker="o", linewidth=2, color="#D73027")
    axes[3].set_title("Monthly Sales Trend")
    axes[3].set_xlabel("Month")
    axes[3].set_ylabel("Net Sales ($)")
    avg_by_discount.plot(kind="bar", ax=axes[4], color=["#66C2A5", "#FC8D62"])
    axes[4].set_title("Average Order Value by Discount Status")
    axes[4].set_ylabel("Average Order Value ($)")
    sns.histplot(df["quantity"], bins=12, kde=False, color="#8DA0CB", ax=axes[5])
    axes[5].set_title("Order Quantity Distribution")
    axes[5].set_xlabel("Quantity")
    axes[5].set_ylabel("Order Count")
    sns.boxplot(x=delay_data, color="#E78AC3", ax=axes[6])
    axes[6].set_title("Shipping Delay Distribution (days)")
    axes[6].set_xlabel("Delay Days")
    sns.histplot(order_value, bins=20, kde=True, color="#66C2A5", ax=axes[7])
    axes[7].set_title("Order Value Distribution")
    axes[7].set_xlabel("Order Value ($)")
    axes[7].set_ylabel("Order Count")
    sns.heatmap(category_month, annot=True, fmt=".0f", cmap="YlGnBu", ax=axes[8], cbar_kws={"label": "Net Sales ($)"})
    axes[8].set_title("Category vs. Month Net Sales")
    axes[8].set_xlabel("Month")
    axes[8].set_ylabel("Category")
    plt.tight_layout()
    save_chart(fig, output_path)


def main() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Missing expected file: {DATA_FILE}")

    df = load_orders(DATA_FILE)

    print_section("ORDER DATA OVERVIEW")
    print(f"Dataset rows: {len(df):,}")
    print(f"Time span: {df['order_date'].min().date()} to {df['order_date'].max().date()}")
    print(f"Unique customers: {df['name'].nunique():,}")
    print(f"Unique products: {df['product'].nunique():,}")
    print(f"Missing shipping dates: {df['shipping_date'].isna().sum():,}")

    print_section("SALES SUMMARY")
    print(f"Total gross revenue: ${df['gross_value'].sum():,.2f}")
    print(f"Total net revenue: ${df['total_value'].sum():,.2f}")
    print(f"Average order value: ${df['total_value'].mean():,.2f}")
    print(f"Median order value: ${df['total_value'].median():,.2f}")
    print(f"Average discount per order: ${df['discount'].mean():,.2f}")

    category_stats = (
        df.groupby("category")
        .agg(
            total_sales=("total_value", "sum"),
            avg_order=("total_value", "mean"),
            order_count=("total_value", "count"),
            quantity_sold=("quantity", "sum"),
            total_discount=("discount", "sum"),
        )
        .sort_values("total_sales", ascending=False)
        .round(2)
    )
    print_section("CATEGORY PERFORMANCE")
    print(category_stats.to_string())

    payment_stats = (
        df.groupby("payment_method")
        .agg(
            total_sales=("total_value", "sum"),
            avg_order=("total_value", "mean"),
            order_count=("total_value", "count"),
        )
        .sort_values("total_sales", ascending=False)
        .round(2)
    )
    print_section("PAYMENT METHOD ANALYSIS")
    print(payment_stats.to_string())

    customer_stats = (
        df.groupby("name")
        .agg(
            total_spent=("total_value", "sum"),
            avg_order=("total_value", "mean"),
            order_count=("total_value", "count"),
        )
        .sort_values("total_spent", ascending=False)
        .head(10)
        .round(2)
    )
    print_section("TOP CUSTOMERS")
    print(customer_stats.to_string())

    repeat_customers = (
        df.reset_index().groupby("name")["id"].count().reset_index(name="order_count")
    )
    repeat_customers = repeat_customers[repeat_customers["order_count"] > 1]
    repeat_rate = len(repeat_customers) / df["name"].nunique() * 100
    print(f"\nRepeat customers: {len(repeat_customers):,}")
    print(f"Repeat purchase rate: {repeat_rate:.1f}%")

    product_stats = (
        df.groupby("product")
        .agg(
            total_sales=("total_value", "sum"),
            avg_order=("total_value", "mean"),
            order_count=("total_value", "count"),
            quantity_sold=("quantity", "sum"),
        )
        .sort_values("total_sales", ascending=False)
        .head(10)
        .round(2)
    )
    print_section("PRODUCT PERFORMANCE")
    print(product_stats.to_string())

    print_section("DISCOUNT INSIGHTS")
    discount_orders = df[df["discount"] > 0]
    discount_rate = len(discount_orders) / len(df) * 100
    print(f"Orders with discount: {len(discount_orders):,} ({discount_rate:.1f}%)")
    print(f"Average discount when offered: ${discount_orders['discount'].mean():,.2f}")
    print(f"Maximum discount: ${discount_orders['discount'].max():,.2f}")

    monthly_stats = (
        df.groupby("order_month")
        .agg(
            total_sales=("total_value", "sum"),
            order_count=("total_value", "count"),
            avg_order=("total_value", "mean"),
        )
        .sort_index()
        .round(2)
    )
    print_section("MONTHLY TREND ANALYSIS")
    print(monthly_stats.to_string())

    print_section("SHIPPING PERFORMANCE")
    shipping_stats = df["shipping_delay_days"].dropna().describe().round(2)
    print(shipping_stats.to_string())
    delayed_pct = (df["shipping_delay_days"] > 0).mean() * 100
    print(f"Orders shipped after the order date: {delayed_pct:.1f}%")

    save_dashboard(df, OUTPUT_IMAGE)
    print_section("SUMMARY INSIGHTS")

    top_category = category_stats.index[0]
    top_product = product_stats.index[0]
    top_payment = payment_stats.index[0]
    top_customer = customer_stats.index[0]

    print(f"Top category: {top_category} with ${category_stats.iloc[0].total_sales:,.2f}")
    print(f"Top product: {top_product} with ${product_stats.iloc[0].total_sales:,.2f}")
    print(f"Most valuable payment method: {top_payment} with ${payment_stats.iloc[0].total_sales:,.2f}")
    print(f"Best customer: {top_customer} spent ${customer_stats.iloc[0].total_spent:,.2f}")
    print(f"Highest sales month: {monthly_stats['total_sales'].idxmax()} (${monthly_stats['total_sales'].max():,.2f})")
    print(f"Dashboard saved to: {OUTPUT_IMAGE}")


if __name__ == "__main__":
    main()











