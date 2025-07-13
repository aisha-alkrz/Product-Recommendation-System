import sqlite3 as sql
import pandas as pd

# Load datasets
products_df = pd.read_csv("data/Extended_Products_Dataset__25_Products.csv")
invoices_df = pd.read_csv("data/Invoices_Dataset_for_Association_Rules.csv")

# Normalize columns: lowercase, no spaces
products_df.columns = products_df.columns.str.strip().str.lower().str.replace(' ', '_')
invoices_df.columns = invoices_df.columns.str.strip().str.lower().str.replace(' ', '_')

print(products_df.columns.tolist())  # تأكد أسماء الأعمدة

conn = sql.connect("data/products.db")
cursor = conn.cursor()

for _, row in products_df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO Products (
                product_id, name, category, price, brand, rating,
                stock, warranty_years, supplier_country,
                weight_kg, volume_cm3, power_watt,
                connectivity_type, material_type, usage_type, price_category
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row['productid'], row['productname'], row['category'], row['price'], row['brand'], row['rating'],
            row['stock'], row['warrantyyears'], row['suppliercountry'],
            row['weightkg'], row['volumecm3'], row['powerwatt'],
            row['connectivitytype'], row['materialtype'], row['usagetype'], row['pricecategory']
        ))
    except Exception as e:
        print(f"❌ Skipping product row due to error: {e}")
        continue

# Insert invoices similarly with normalized columns
for _, row in invoices_df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO Invoices (invoice_id, product_id)
            VALUES (?, ?)
        """, (row['invoiceid'], row['productid']))
    except Exception as e:
        print(f"❌ Skipping invoice row due to error: {e}")
        continue

conn.commit()
conn.close()

print("✅ Data inserted into the database successfully.")
