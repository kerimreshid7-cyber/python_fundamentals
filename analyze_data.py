from pathlib import Path

import numpy as np
import pandas as pd

DATA_FILE = Path(__file__).parent / "data_insertion.csv"


def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['shipping_date'] = pd.to_datetime(df['shipping_date'], errors='coerce')
    df['discount'] = df['discount'].fillna(0.0)
    df['payment_method'] = df['payment_method'].fillna('Unknown')
    df['email'] = df['email'].fillna('missing@example.com')
    df['phone'] = df['phone'].replace({np.nan: None})
    df['total_value'] = (df['price'] * df['quantity']) - df['discount']
    df['gross_value'] = df['price'] * df['quantity']
    df['shipping_delay_days'] = (df['shipping_date'] - df['order_date']).dt.days
    return df


def print_section(title: str) -> None:
    print('\n' + '=' * 80)
    print(title)
    print('=' * 80)


def main() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Data file not found: {DATA_FILE}")

    df = load_data(DATA_FILE)

    print_section('ORDER DATA SUMMARY')
    print(f'Total records: {len(df):,}')
    print(f'Date range: {df["order_date"].min().date()} to {df["order_date"].max().date()}')
    print(f'Unique customers: {df["name"].nunique():,}')
    print(f'Unique products: {df["product"].nunique():,}')
    print('\nMissing values by column:')
    print(df.isna().sum())

    print_section('SALES METRICS')
    print(f'Total gross sales: ${df["gross_value"].sum():,.2f}')
    print(f'Total net sales (after discounts): ${df["total_value"].sum():,.2f}')
    print(f'Average order value: ${df["total_value"].mean():,.2f}')
    print(f'Median order value: ${df["total_value"].median():,.2f}')
    print(f'Total discounts given: ${df["discount"].sum():,.2f}')

    print_section('CATEGORY PERFORMANCE')
    category_stats = (
        df.groupby('category')
        .agg(
            total_sales=('total_value', 'sum'),
            average_order=('total_value', 'mean'),
            order_count=('id', 'count'),
            total_quantity=('quantity', 'sum'),
            total_discount=('discount', 'sum'),
        )
        .sort_values('total_sales', ascending=False)
    )
    print(category_stats.round(2).to_string())

    print_section('TOP PRODUCTS')
    top_products = (
        df.groupby('product')
        .agg(
            total_sales=('total_value', 'sum'),
            order_count=('id', 'count'),
            total_quantity=('quantity', 'sum'),
        )
        .sort_values('total_sales', ascending=False)
        .head(10)
    )
    print(top_products.round(2).to_string())

    print_section('PAYMENT METHOD ANALYSIS')
    payment_stats = (
        df.groupby('payment_method')
        .agg(
            total_sales=('total_value', 'sum'),
            average_order=('total_value', 'mean'),
            order_count=('id', 'count'),
        )
        .sort_values('total_sales', ascending=False)
    )
    print(payment_stats.round(2).to_string())

    print_section('DISCOUNT ANALYSIS')
    discounts = df['discount'].fillna(0.0)
    orders_with_discount = (discounts > 0).sum()
    print(f'Orders with discount: {orders_with_discount:,} ({orders_with_discount / len(df) * 100:.1f}%)')
    print(f'Average discount per order: ${discounts.mean():,.2f}')
    print(f'Max discount: ${discounts.max():,.2f}')

    print_section('MONTHLY SALES TRENDS')
    df['order_month'] = df['order_date'].dt.to_period('M')
    monthly_stats = (
        df.groupby('order_month')
        .agg(
            total_sales=('total_value', 'sum'),
            order_count=('id', 'count'),
            average_order=('total_value', 'mean'),
        )
        .sort_index()
    )
    print(monthly_stats.round(2).to_string())

    print_section('SHIPPING PERFORMANCE')
    shipping_stats = df['shipping_delay_days'].describe()
    print(shipping_stats.round(2).to_string())
    delayed = df['shipping_delay_days'] > 0
    print(f'Orders with shipping delay: {delayed.sum():,} ({delayed.mean() * 100:.1f}%)')

    print_section('TOP CUSTOMERS')
    customer_stats = (
        df.groupby('name')
        .agg(
            total_spent=('total_value', 'sum'),
            order_count=('id', 'count'),
        )
        .sort_values('total_spent', ascending=False)
        .head(10)
    )
    print(customer_stats.round(2).to_string())

    print_section('KEY INSIGHTS')
    top_category = category_stats.index[0]
    print(f'Top category by net sales: {top_category} (${category_stats.iloc[0].total_sales:,.2f})')
    top_product = top_products.index[0]
    print(f'Highest revenue product: {top_product} (${top_products.iloc[0].total_sales:,.2f})')
    best_payment = payment_stats.index[0]
    print(f'Most valuable payment method: {best_payment} (${payment_stats.iloc[0].total_sales:,.2f})')


if __name__ == '__main__':
    main()
