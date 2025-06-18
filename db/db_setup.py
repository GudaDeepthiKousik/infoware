# db/db_setup.py

import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1603",  # replace with your actual MySQL password
        database="db"
    )

def initialize_db():
    db = create_connection()
    cursor = db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS operators (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE,
        password VARCHAR(50)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        barcode VARCHAR(100),
        sku_id VARCHAR(100),
        category VARCHAR(100),
        subcategory VARCHAR(100),
        image_path TEXT,
        product_name VARCHAR(255),
        description TEXT,
        tax FLOAT,
        price FLOAT,
        default_unit VARCHAR(50)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goods_receiving (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product_id INT,
        supplier_details TEXT,
        quantity FLOAT,
        unit VARCHAR(50),
        rate_per_unit FLOAT,
        total_rate FLOAT,
        tax FLOAT,
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product_id INT,
        customer_details TEXT,
        quantity FLOAT,
        unit VARCHAR(50),
        rate_per_unit FLOAT,
        total_rate FLOAT,
        tax FLOAT,
        FOREIGN KEY (product_id) REFERENCES products(id)
    )
    """)

    # Insert two operator logins
    cursor.execute("INSERT IGNORE INTO operators (username, password) VALUES ('operator1', 'pass1'), ('operator2', 'pass2')")

    db.commit()
    db.close()
if __name__ == "__main__":
    initialize_db()
    print("Tables created successfully!") 