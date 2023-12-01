import pymysql
from db.Conection import connectionBD as db


class Product():
    def __init__(self):
        self.connection = db()
        self.cursor = self.connection.cursor()

    def get_all_products(self):
        try:
            self.cursor.execute(
                "SELECT p.id_product, p.name AS product_name, p.description, p.price, p.stock, c.name AS category_name FROM products p INNER JOIN product_categories c ON p.id_category = c.id_category")
            result = self.cursor.fetchall()
            return result
        except pymysql.Error as e:
            return f'Error: {e}'
        finally:
            self.cursor.close()
            self.connection.close()

    def get_single_product(self, id_product):
        try:
            self.cursor.execute(
                f"SELECT * FROM products WHERE id = {id_product}")
            result = self.cursor.fetchone()
            return result
        except pymysql.Error as e:
            return f'Error: {e}'
        finally:
            self.cursor.close()
            self.connection.close()

    def update_product(self, id_product, name, description, price, stock, id_category):
        try:
            sql = f"UPDATE products SET name = '{name}', description = '{description}', price = {price}, stock = {stock}, id_category = {id_category} WHERE id = {id_product}"
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except pymysql.Error as e:
            return f'Error: {e}'
        finally:
            self.cursor.close()
            self.connection.close()

    def delete_product(self, id_product):
        try:
            sql = f"DELETE FROM products WHERE id = {id_product}"
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except pymysql.Error as e:
            return f'Error: {e}'
        finally:
            self.cursor.close()
            self.connection.close()
