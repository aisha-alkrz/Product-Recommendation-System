import sqlite3 as sql;

conn = sql.connect("data/products.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    brand TEXT,
    type TEXT,
    color TEXT,
    category_id INTEGER,
    cluster_id_no_price INTEGER,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);
""")