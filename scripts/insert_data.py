import sqlite3 as sql

# Connect to the database
conn = sql.connect("data/products.db")
cursor = conn.cursor()


# Insert categories 

categories = [
    ("Electronics",),
    ("Cosmetics",),
    ("Furniture",)
]

cursor.executemany("INSERT INTO Categories (name) VALUES (?)", categories)
conn.commit()