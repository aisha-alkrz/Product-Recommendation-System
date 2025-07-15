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
