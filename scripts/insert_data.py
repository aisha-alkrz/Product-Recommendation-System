import sqlite3 as sql

# Connect to the database
conn = sql.connect("data/products.db")
cursor = conn.cursor()
