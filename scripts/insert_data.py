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


# Insert products
products = [
    ("Laptop HP 15", 1200.0, "HP", "Laptop", "Silver", 1, None),
    ("Gaming Mouse", 45.0, "Logitech", "Mouse", "Black", 1, None),
    ("Red Lipstick", 25.0, "Maybelline", "Lipstick", "Red", 2, None),
    ("Foundation Cream", 60.0, "L'Oréal", "Foundation", "Beige", 2, None),
    ("Office Desk", 350.0, "IKEA", "Desk", "Brown", 3, None),
    ("Desk Lamp", 40.0, "Philips", "Lamp", "White", 3, None),
    ("Monitor LG 27\"", 700.0, "LG", "Monitor", "Black", 1, None),
    ("Bluetooth Headphones", 130.0, "Sony", "Headphones", "Black", 1, None),
    ("Compact Powder", 30.0, "Rimmel", "Powder", "Light Beige", 2, None),
    ("Eyeliner Pen", 18.0, "Essence", "Eyeliner", "Black", 2, None),
    ("Bookshelf", 280.0, "HomeStyle", "Shelf", "Walnut", 3, None),
    ("Makeup Brush Set", 50.0, "Sigma", "Brushes", "Rose Gold", 2, None),
    ("LED Strip Light", 22.0, "Xiaomi", "Light", "RGB", 1, None),
    ("Face Serum", 90.0, "The Ordinary", "Serum", "Clear", 2, None),
    ("Smartphone", 950.0, "Samsung", "Phone", "Blue", 1, None),
    ("Cushion Chair", 190.0, "ComfortHome", "Chair", "Grey", 3, None),
    ("Keyboard Mechanical", 85.0, "Corsair", "Keyboard", "Black", 1, None),
    ("Blush Palette", 35.0, "NYX", "Blush", "Mixed", 2, None),
    ("Bedside Table", 145.0, "IKEA", "Table", "White", 3, None),
    ("USB-C Hub", 39.0, "Anker", "Accessory", "Gray", 1, None)
]

cursor.executemany("""
INSERT INTO Products (name, price, brand, type, color, category_id, cluster_id_no_price)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", products)
conn.commit()



relations = [
    (1, 2, 0.85),   # Laptop → Mouse
    (3, 4, 0.75),   # Lipstick → Foundation
    (5, 6, 0.65),   # Desk → Lamp
    (2, 17, 0.7),   # Mouse → Keyboard
    (4, 9, 0.6),    # Foundation → Powder
    (14, 13, 0.5),  # Serum → LED Light 
    (3, 10, 0.6),   # Lipstick → Eyeliner
    (11, 19, 0.55), # Bookshelf → Table
    (8, 20, 0.7),   # Headphones → USB-C Hub
    (12, 18, 0.65)  # Brush Set → Blush Palette
]

cursor.executemany("""
INSERT INTO ProductRelations (base_product_id, related_product_id, similarity_score)
VALUES (?, ?, ?)
""", relations)
conn.commit()
conn.close()

print("Successfully inserted", len(categories), "categories and", len(products), "products" , len(relations), "ProductRelations")