import sqlite3
import random
import string

class ProductDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                price REAL
                                )''')
        self.conn.commit()

    def insert_product(self, name, price):
        self.cursor.execute('''INSERT INTO products (name, price) VALUES (?, ?)''', (name, price))
        self.conn.commit()

    def update_product_price(self, product_id, new_price):
        self.cursor.execute('''UPDATE products SET price=? WHERE id=?''', (new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''DELETE FROM products WHERE id=?''', (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        self.cursor.execute('''SELECT * FROM products WHERE id=?''', (product_id,))
        return self.cursor.fetchone()

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_sample_data():
    sample_data = []
    for _ in range(100):
        name = generate_random_string(8)
        price = random.uniform(10, 1000)  # 임의의 가격 생성
        sample_data.append((name, price))
    return sample_data

# 데이터베이스 생성
db = ProductDatabase("products.db")

# 샘플 데이터 생성 및 삽입
sample_data = generate_sample_data()
for name, price in sample_data:
    db.insert_product(name, price)

# 제품 조회 예시
product_id = 1
print("Selected Product:", db.select_product(product_id))

# 제품 가격 업데이트 예시
new_price = 500.0
db.update_product_price(product_id, new_price)
print("Updated Product Price:", db.select_product(product_id))

# 제품 삭제 예시
db.delete_product(product_id)
print("Deleted Product:", db.select_product(product_id))

