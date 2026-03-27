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

    df['Revenue'] = df['Quantity'] * df['Price']

    return df

df = load_data()

avg_revenue, total_bill, count_of_sales = st.columns(3)

avg_revenue.metric('Average revenue from all sales', round(df['Revenue'].mean(), 2))
total_bill.metric('Total bill of all sales', round(df['Revenue'].sum(), 2))
count_of_sales.metric('Count of all sales', round(df['Revenue'].count(), 2))