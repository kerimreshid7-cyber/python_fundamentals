
import plotly as plt
import pandas as pd

df = pd.read_csv("data/orders.csv",index_col='id')

print(df.head())
print(df.shape)
print()
print('=========================how to get all columns=======================')
print(df.columns)


columns = ['name', 'email', 'phone', 'payment_method', 'product', 'category',
           'price', 'quantity', 'discount', 'order_date', 'shipping_date']

# Data preprocessing
df['order_date'] = pd.to_datetime(df['order_date'])
df['year_month'] = df['order_date'].dt.to_period('M')
df['total_value'] = (df['price'] * df['quantity']) - df['discount'].fillna(0)

print("=" * 80)
print("COMPREHENSIVE ORDERS ANALYSIS")
print("=" * 80)

# 1. CATEGORY ANALYSIS
print("\n📊 CATEGORY PERFORMANCE ANALYSIS")
print("-" * 50)
category_stats = df.groupby('category').agg({
    'total_value': ['sum', 'mean', 'count'],
    'quantity': 'sum',
    'discount': 'sum'
}).round(2)
category_stats.columns = ['Total Sales', 'Avg Order Value', 'Order Count', 'Total Quantity', 'Total Discount']
category_stats = category_stats.sort_values('Total Sales', ascending=False)
print(category_stats)

# # 2. PAYMENT METHOD ANALYSIS
# print("\n💳 PAYMENT METHOD ANALYSIS")
# print("-" * 50)
# payment_stats = df.groupby('payment_method').agg({
#     'total_value': ['sum', 'mean', 'count'],
#     'discount': 'sum'
# }).round(2)
# payment_stats.columns = ['Total Sales', 'Avg Order Value', 'Order Count', 'Total Discount']
# payment_stats = payment_stats.sort_values('Total Sales', ascending=False)
# print(payment_stats)

# # 3. CUSTOMER ANALYSIS
# print("\n👥 CUSTOMER ANALYSIS")
# print("-" * 50)
# customer_stats = df.groupby('customer_name').agg({
#     'total_value': ['sum', 'mean', 'count'],
#     'order_id': 'count'
# }).round(2)
# customer_stats.columns = ['Total Spent', 'Avg Order Value', 'Order Count', 'Order Count2']
# customer_stats = customer_stats.sort_values('Total Spent', ascending=False).head(10)
# print("Top 10 Customers by Total Spending:")
# print(customer_stats)

# # Repeat customers analysis
# repeat_customers = df.groupby('customer_name').size().reset_index(name='order_count')
# repeat_customers = repeat_customers[repeat_customers['order_count'] > 1]
# print(f"\n📈 Repeat Customers: {len(repeat_customers)} out of {df['customer_name'].nunique()} unique customers")
# print(f"Repeat Rate: {len(repeat_customers)/df['customer_name'].nunique()*100:.1f}%")

# # 4. PRODUCT PERFORMANCE
# print("\n🛍️  PRODUCT PERFORMANCE ANALYSIS")
# print("-" * 50)
# product_stats = df.groupby('product_name').agg({
#     'total_value': ['sum', 'mean', 'count'],
#     'quantity': 'sum'
# }).round(2)
# product_stats.columns = ['Total Revenue', 'Avg Order Value', 'Order Count', 'Total Quantity']
# product_stats = product_stats.sort_values('Total Revenue', ascending=False)
# print(product_stats)

# # 5. DISCOUNT ANALYSIS
# print("\n💰 DISCOUNT ANALYSIS")
# print("-" * 50)
# discount_analysis = {
#     'Orders with Discount': df[df['discount'].notna()].shape[0],
#     'Orders without Discount': df[df['discount'].isna()].shape[0],
#     'Total Discount Given': df['discount'].sum(),
#     'Average Discount': df['discount'].mean(),
#     'Max Discount': df['discount'].max()
# }
# for key, value in discount_analysis.items():
#     if isinstance(value, float):
#         print(f"{key}: ${value:.2f}")
#     else:
#         print(f"{key}: {value}")

# # 6. MONTHLY TRENDS
# print("\n📅 MONTHLY TRENDS ANALYSIS")
# print("-" * 50)
# monthly_stats = df.groupby('year_month').agg({
#     'total_value': ['sum', 'mean', 'count'],
#     'quantity': 'sum',
#     'discount': 'sum'
# }).round(2)
# monthly_stats.columns = ['Total Sales', 'Avg Order Value', 'Order Count', 'Total Quantity', 'Total Discount']
# monthly_stats = monthly_stats.sort_index(ascending=False)
# print(monthly_stats)

# # Create comprehensive visualizations
# plt.style.use('seaborn-v0_8')
# fig = plt.figure(figsize=(20, 16))

# # 1. Category Sales Pie Chart
# ax1 = plt.subplot(3, 3, 1)
# category_sales = df.groupby('category')['total_value'].sum()
# colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
# ax1.pie(category_sales.values, labels=category_sales.index, autopct='%1.1f%%', colors=colors, startangle=90)
# ax1.set_title('Sales by Category', fontsize=14, fontweight='bold')

# # 2. Payment Methods Bar Chart
# ax2 = plt.subplot(3, 3, 2)
# payment_sales = df.groupby('payment_method')['total_value'].sum().sort_values(ascending=True)
# payment_sales.plot(kind='barh', ax=ax2, color='#FF6B6B')
# ax2.set_title('Total Sales by Payment Method', fontsize=14, fontweight='bold')
# ax2.set_xlabel('Total Sales ($)')

# # 3. Top Customers Bar Chart
# ax3 = plt.subplot(3, 3, 3)
# top_customers = df.groupby('customer_name')['total_value'].sum().sort_values(ascending=False).head(8)
# top_customers.plot(kind='bar', ax=ax3, color='#4ECDC4')
# ax3.set_title('Top 8 Customers by Spending', fontsize=14, fontweight='bold')
# ax3.set_xlabel('Customer Name')
# ax3.set_ylabel('Total Sales ($)')
# ax3.tick_params(axis='x', rotation=45)

# # 4. Monthly Sales Trend
# ax4 = plt.subplot(3, 3, 4)
# monthly_trend = df.groupby('year_month')['total_value'].sum()
# monthly_trend.plot(kind='line', ax=ax4, marker='o', linewidth=2, markersize=8, color='#FF6B9D')
# ax4.set_title('Monthly Sales Trend', fontsize=14, fontweight='bold')
# ax4.set_xlabel('Month')
# ax4.set_ylabel('Total Sales ($)')
# ax4.tick_params(axis='x', rotation=45)
# ax4.grid(True, alpha=0.3)

# # 5. Product Performance
# ax5 = plt.subplot(3, 3, 5)
# top_products = df.groupby('product_name')['total_value'].sum().sort_values(ascending=False).head(6)
# top_products.plot(kind='bar', ax=ax5, color='#C9B1FF')
# ax5.set_title('Top 6 Products by Revenue', fontsize=14, fontweight='bold')
# ax5.set_xlabel('Product Name')
# ax5.set_ylabel('Total Revenue ($)')
# ax5.tick_params(axis='x', rotation=45)

# # 6. Order Value Distribution
# ax6 = plt.subplot(3, 3, 6)
# ax6.hist(df['total_value'], bins=20, color='#95E1D3', alpha=0.7, edgecolor='black')
# ax6.set_title('Order Value Distribution', fontsize=14, fontweight='bold')
# ax6.set_xlabel('Order Value ($)')
# ax6.set_ylabel('Frequency')
# ax6.axvline(df['total_value'].mean(), color='red', linestyle='--', label=f'Mean: ${df["total_value"].mean():.0f}')
# ax6.legend()

# # 7. Discount Impact
# ax7 = plt.subplot(3, 3, 7)
# discount_impact = df.groupby(df['discount'].notna())['total_value'].mean()
# discount_impact.index = ['No Discount', 'With Discount']
# discount_impact.plot(kind='bar', ax=ax7, color=['#FFB6C1', '#FFA07A'])
# ax7.set_title('Average Order Value: Discount Impact', fontsize=14, fontweight='bold')
# ax7.set_ylabel('Average Order Value ($)')
# ax7.tick_params(axis='x', rotation=0)

# # 8. Quantity Distribution
# ax8 = plt.subplot(3, 3, 8)
# quantity_dist = df['quantity'].value_counts().sort_index()
# quantity_dist.plot(kind='bar', ax=ax8, color='#87CEEB')
# ax8.set_title('Quantity per Order Distribution', fontsize=14, fontweight='bold')
# ax8.set_xlabel('Quantity')
# ax8.set_ylabel('Number of Orders')
# ax8.tick_params(axis='x', rotation=0)

# 9. Heatmap of Sales by Category and Month
ax9 = plt.subplot(3, 3, 9)
category_month = df.pivot_table(values='total_value', index='category', columns='year_month', aggfunc='sum', fill_value=0)
sns.heatmap(category_month, annot=True, fmt='.0f', cmap='YlOrRd', ax=ax9, cbar_kws={'label': 'Sales ($)'})
ax9.set_title('Sales Heatmap: Category vs Month', fontsize=14, fontweight='bold')
ax9.set_xlabel('Month')
ax9.set_ylabel('Category')

plt.tight_layout()
plt.savefig('/home/kerim/CascadeProjects/comprehensive_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()

# Generate Key Insights Summary
print("\n" + "=" * 80)
print("🎯 KEY BUSINESS INSIGHTS")
print("=" * 80)

insights = []

# Category insights
top_category = category_stats.index[0]
category_revenue = category_stats.loc[top_category, 'Total Sales']
category_percentage = (category_revenue / df['total_value'].sum()) * 100
insights.append(f"🏆 {top_category} dominates with ${category_revenue:,.0f} ({category_percentage:.1f}% of total sales)")

# Payment method insights
top_payment = payment_stats.index[0]
payment_percentage = (payment_stats.loc[top_payment, 'Total Sales'] / df['total_value'].sum()) * 100
insights.append(f"💳 {top_payment} is preferred payment method ({payment_percentage:.1f}% of transactions)")

# Customer insights
top_customer = customer_stats.index[0]
customer_spending = customer_stats.loc[top_customer, 'Total Spent']
insights.append(f"👤 Best customer: {top_customer} spent ${customer_spending:,.0f}")

# Product insights
top_product = product_stats.index[0]
product_revenue = product_stats.loc[top_product, 'Total Revenue']
insights.append(f"🛍️  Best-selling product: {top_product} generated ${product_revenue:,.0f}")

# Discount insights
discount_rate = (df[df['discount'].notna()].shape[0] / df.shape[0]) * 100
insights.append(f"💰 {discount_rate:.1f}% of orders include discounts")

# Monthly insights
best_month = monthly_stats['Total Sales'].idxmax()
worst_month = monthly_stats['Total Sales'].idxmin()
insights.append(f"📅 Peak month: {best_month}, Lowest: {worst_month}")

# Customer retention insights
insights.append(f"🔄 {len(repeat_customers)} customers made repeat purchases ({len(repeat_customers)/df['customer_name'].nunique()*100:.1f}% repeat rate)")

# Average order value
insights.append(f"📊 Average order value: ${df['total_value'].mean():.0f}")

for insight in insights:
    print(insight)

print(f"\n📈 Total Revenue: ${df['total_value'].sum():,.2f}")
print(f"🛒 Total Orders: {len(df)}")
print(f"👥 Unique Customers: {df['customer_name'].nunique()}")
print(f"📅 Analysis Period: {df['order_date'].min().strftime('%Y-%m-%d')} to {df['order_date'].max().strftime('%Y-%m-%d')}")

print(f"\n🎨 Comprehensive dashboard saved as 'comprehensive_dashboard.png'")
print("✅ Analysis Complete!")











