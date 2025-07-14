import sqlite3
import pandas as pd
import streamlit as st

# === Step 1: Load Products from DB ===
conn = sqlite3.connect("Data/products.db")
products_df = pd.read_sql_query("SELECT * FROM Products", conn)
conn.close()

# === Step 2: Load Apriori rules ===
rules = pd.read_csv("Data/apriori_rules.csv")
rules["antecedents"] = rules["antecedents"].apply(eval)
rules["consequents"] = rules["consequents"].apply(eval)
# === Step 3: Product Selection UI ===
st.title("🛍 Product Recommendation System")
product_names = products_df["name"].tolist()
selected_product = st.selectbox("Select a product", product_names)

selected_row = products_df[products_df["name"] == selected_product].iloc[0]
selected_id = selected_row["product_id"]
selected_cluster = selected_row["cluster_id_with_price"]

st.markdown(f"### Selected Product ID: {selected_id}")
st.markdown(f"Cluster ID: {selected_cluster}")
