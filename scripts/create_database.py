import sqlite3 as sql;

# Connect to SQLite database (or create it if it doesn't exist)
conn = sql.connect("data/products.db")
cursor = conn.cursor()

# Create the Products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    brand TEXT,
    rating REAL,
    stock INTEGER,
    warranty_years INTEGER,
    supplier_country TEXT,
    weight_kg REAL,
    volume_cm3 REAL,
    power_watt REAL,
    connectivity_type TEXT,
    material_type TEXT,
    usage_type TEXT,
    price_category TEXT
);
""")

# Create the Invoices table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Invoices (
    invoice_id INTEGER,
    product_id INTEGER,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
""")

# Save changes and close the connection
conn.commit()
conn.close()

print("✅ Database and tables created successfully.")