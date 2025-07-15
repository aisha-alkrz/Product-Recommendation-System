import streamlit as st
import pandas as pd

# Load datasets
clustered_with_price = pd.read_csv("data/products_names_with_clusters_with_price.csv")
clustered_without_price = pd.read_csv("data/products_names_with_clusters_without_price.csv")
apriori_rules = pd.read_csv("data/apriori_rules.csv")
