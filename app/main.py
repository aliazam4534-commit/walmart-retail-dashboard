import streamlit as st
import pandas as pd

st.set_page_config(page_title="Walmart Reatil Dashboard")

st.title("Walmart Retail Dashboard")

df = pd.read_csv("data/sales.csv")

df["revenue"] = df["price"] * df["quantity"]

total_revenue = df["revenue"].sum()
total_items = df["quantity"].sum()
avg_revenue_per_item = total_revenue / total_items

top_product = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .idxmax()
)

top_category = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .idxmax()
)

st.subheader("Key Performance Indicators")

col1, col2 , col3 , col4 , col5 = st.columns(5)

col1.metric("Total Revenue", f"${total_revenue}")
col2.metric("Total Items Sold", total_items)
col3.metric("Avg Revenue per Item", f"${round(avg_revenue_per_item, 2)}")
col4.metric("Top Product", top_product)
col5.metric("Top Category", top_category)

st.subheader("Sales Data")
st.dataframe(df)