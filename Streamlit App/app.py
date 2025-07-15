import sqlite3
import pandas as pd
import streamlit as st

# === Step 1: Load Products from DB ===
conn = sqlite3.connect("Data/products.db")
products_df = pd.read_sql_query("SELECT * FROM Products", conn)
conn.close()
