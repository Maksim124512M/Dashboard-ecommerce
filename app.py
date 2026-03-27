import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_excel('data/online_retail.xlsx')

# # General information
# print(f'First 5 dataframe: {df.head()}')
# print(f'Last 5 dataframe: {df.tail()}')
# print(f'Info about dataframe: {df.info()}')
# print(f'Dataframe description: {df.describe()}')

# # Dublicates and NaN's
# print(f'NaN values in dataframe: \n {df.isna().sum()}')
# print(f'Duplicates in dataframe: \n {df.duplicated().sum()}')

# # Handling of NaN values and duplicates
# df = df.drop_duplicates()
# df['Description'] = df['Description'].fillna(df['Description'].mode()[0])
# df['Customer ID'] = df['Customer ID'].fillna(df['Customer ID'].median())

@st.cache_data
def load_data():
    df = pd.read_excel('data/online_retail.xlsx')
    df = df.drop_duplicates()

    df['Description'] = df['Description'].fillna(df['Description'].mode()[0])
    df['Customer ID'] = df['Customer ID'].fillna(df['Customer ID'].median())
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%d.%m.%Y %H:%M')
    df['YearMonth'] = df['InvoiceDate'].dt.to_period('M')

    df['Revenue'] = df['Quantity'] * df['Price']

    return df

df = load_data()

avg_revenue, total_bill, count_of_sales = st.columns(3)

avg_revenue.metric('Average revenue from all sales', round(df['Revenue'].mean(), 2))
total_bill.metric('Total bill of all sales', round(df['Revenue'].sum(), 2))
count_of_sales.metric('Count of all sales', round(df['Revenue'].count(), 2))

monthly_revenue = df.groupby('InvoiceDate')['Revenue'].sum()
top_five_products  = df.groupby(['StockCode', 'Description'])['Revenue'].sum().sort_values(ascending=False).head().reset_index()

fig = make_subplots(
    rows=2, cols=1, 
    subplot_titles=('Revenue by dates', 'TOP-5 products by revenue')
)

fig.add_trace(go.Scatter(
    x=monthly_revenue.index,
    y=monthly_revenue.values,
    mode='lines+markers',
    name='Revenue',
), row=1, col=1)

fig.add_trace(go.Bar(
    x=top_five_products['StockCode'].astype(str),
    y=top_five_products['Revenue'],
    name='StockCode',
), row=2, col=1)

fig.update_layout(
    title='Online retail dashboard',
    template='plotly_dark',
    width=1600,
    height=600,
    showlegend=True,
)

st.plotly_chart(fig)