import streamlit as st
import pandas as pd

# Load datasets
clustered_with_price = pd.read_csv("data/products_names_with_clusters_with_price.csv")
clustered_without_price = pd.read_csv("data/products_names_with_clusters_without_price.csv")
apriori_rules = pd.read_csv("data/apriori_rules.csv")
# Page title and style
st.set_page_config(page_title="Product Recommendation System", layout="centered")
st.title("🛒 Product Recommendation System")

st.markdown("""
<style>
div.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)
# Product selection
all_products = clustered_with_price['productname'].unique()
selected_product = st.selectbox("Select a product:", sorted(all_products))
# Clustering mode selection
mode = st.radio("Choose clustering method:", ["📊 With Price", "🔍 Without Price"])

# Select dataset based on mode
df = clustered_with_price if mode == "📊 With Price" else clustered_without_price

# Get cluster of selected product
product_cluster = df[df['productname'] == selected_product]['cluster'].values[0]
