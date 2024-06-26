import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(
            "C://Users//User//pythonProject" + r"//become_qa_auto.db"
        )
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected succesfully.SQLite Database Version is:{record}")

    def get_all_users(self):
        query = "SELECT name,address,city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_user(self, name, address, city, postalCode, country):
        if not name:
            raise ValueError("Name field cannot be empty")
        if not address:
            raise ValueError("Address field cannot be empty")
        if not city:
            raise ValueError("City field cannot be empty")
        if not postalCode:
            raise ValueError("Postal code field cannot be empty")
        if not country:
            raise ValueError("Country field cannot be empty")

        query = f"INSERT OR REPLACE INTO customers (name,address,city,postalCode,country) \
              VALUES ('{name}','{address}','{city}',{postalCode},'{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    def get_user_address_by_name(self, name):
        query = f"SELECT address,city,postalCode,country,id FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def select_product_by_id(self, product_id):
        query = f"SELECT id,name,description, quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        if not product_id or not isinstance(product_id, int):
            raise ValueError("Id field must be integer")
        if not qnt or not isinstance(qnt, int):
            raise ValueError("Quantity field must be integer")

        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        if not isinstance(product_id, int) or not isinstance(qnt, int):
            raise TypeError("Product id and quantity must be integer")

        query = f"INSERT OR REPLACE INTO products (id,name,description,quantity) \
              VALUES ({product_id},'{name}','{description}',{qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id,customers.name,products.name,products.description, orders.order_date \
        FROM orders JOIN customers ON orders.customer_id = customers.id JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
