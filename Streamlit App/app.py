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
# Show similar products in the same cluster
st.markdown("### 🔗 Products from the same cluster:")
similar_products = df[(df['cluster'] == product_cluster) & (df['productname'] != selected_product)]
if not similar_products.empty:
    st.table(similar_products[['productname']].reset_index(drop=True).rename(columns={"productname": "Similar Product"}))
else:
    st.info("No other products found in the same cluster.")
# Show associated products from Apriori rules
st.markdown("### 🧠 Recommended products (Apriori rules):")
related_rules = apriori_rules[apriori_rules['antecedents'].str.contains(selected_product)]
if not related_rules.empty:
    for _, row in related_rules.iterrows():
        product = list(eval(row['consequents']))[0]
        confidence = row['confidence']
        st.markdown(f"- *{product}* (confidence: {confidence:.2f})")
else:
    st.info("No association rules found for this product.")
