import sqlite3
import random

class ProductManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        # 테이블 생성 (필요한 경우)
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)

    def insert_product(self, product_name, price):
        self.cursor.execute("""
            INSERT INTO products (product_name, price)
            VALUES (?, ?)
        """, (product_name, price))
        self.connection.commit()

    def update_product(self, product_id, product_name, price):
        self.cursor.execute("""
            UPDATE products
            SET product_name = ?, price = ?
            WHERE product_id = ?
        """, (product_name, price, product_id))
        self.connection.commit()

    def delete_product(self, product_id):
        self.cursor.execute("""
            DELETE FROM products
            WHERE product_id = ?
        """, (product_id,))
        self.connection.commit()

    def select_all_products(self):
        self.cursor.execute("""
            SELECT * FROM products
        """)
        return self.cursor.fetchall()

    def select_product_by_id(self, product_id):
        self.cursor.execute("""
            SELECT * FROM products
            WHERE product_id = ?
        """, (product_id,))
        return self.cursor.fetchone()

# 샘플 데이터 준비 (100개)
product_names = [
    "iPhone 14", "Galaxy S23", "AirPods Pro", "MacBook Pro", "iPad Air", "Apple Watch",
    "Google Pixel 7", "Samsung Galaxy Z Fold4", "Microsoft Surface Laptop Studio", "Sony PlayStation 5",
    "LG Gram 17", "Dell XPS 13", "HP Spectre x360", "Lenovo ThinkPad X1 Carbon", "Acer Swift 7",
    "MSI GE66 Raider", "ASUS ROG Zephyrus G15", "Alienware m15 R7", "Razer Blade 15", "GIGABYTE AERO 16",
    "Samsung Galaxy Tab S8 Ultra", "Apple iPad Pro (12.9-inch)", "Microsoft Surface Pro 8", "Lenovo Yoga Tab 13", "Samsung Galaxy Book 2",
    "Sony WH-1000XM5", "Bose QuietComfort 45", "Apple AirPods Max", "Sennheiser Momentum 3 Wireless", "Jabra Elite 7 Pro",
    "Sony Bravia XR A80K", "LG C2 OLED", "Samsung The Frame", "TCL 8-Series Roku TV", "Hisense U8G",
    "Google Nest Hub Max", "Amazon Echo Show 8", "Apple HomePod mini", "Facebook Portal Plus", "Lenovo Smart Display 7",
    "Dyson V15 Detect Absolute", "Shark NV150 Navigator Freestyle", "Hoover H-Clean 900", "Samsung Jet 90 Complete", "LG CordZero A920",
    "iRobot Roomba j7+", "Ecovacs Deebot X1 Omni", "Roborock S7 MaxV Ultra", "Neato D10 Pro", "Eufy RoboVac G30 Hybrid",
    "Nespresso Vertuo Plus", "Breville Bambino Plus", "De'Longhi Dedica EC685M", "Gaggia Classic Pro", "La Pavoni Europiccola",
    "Ninja Foodi Grill + Air Fryer", "Instant Pot Duo Plus", "Breville Smart Oven Air Fryer Pro", "Cuisinart AirFryer Toaster Oven", "Philips Airfryer HD9650/97",
    "Sony Alpha 7 IV", "Canon EOS R6", "Nikon Z5", "Fujifilm X-T4", "Panasonic Lumix GH5 II",
    "DJI Mavic 3", "GoPro HERO10 Black", "Insta360 One X2",]
