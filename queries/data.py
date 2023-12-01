import pymysql
from controllers.product_controller import Product
from controllers.category_controller import Category


class Queries():
    def __init__(self):
        self.products = Product()
        self.categories = Category()

    def get_all_products(self):
        try:
            result = self.products.get_all_products()
            return result
        except pymysql.Error as e:
            return f'Error: {e}'

    def get_single_product(self, id_product):
        try:
            result = self.products.get_single_product(id_product)
            return result
        except pymysql.Error as e:
            return f'Error: {e}'

    def update_product(self, id_product, name, description, price, stock, id_category):
        try:
            result = self.products.update_product(
                id_product, name, description, price, stock, id_category)
            return result
        except pymysql.Error as e:
            return f'Error: {e}'

    def delete_product(self, id_product):
        try:
            result = self.products.delete_product(id_product)
            return result
        except pymysql.Error as e:
            return f'Error: {e}'

    def get_all_categories(self):
        try:
            result = self.categories.get_all_categories()
            return result
        except pymysql.Error as e:
            return f'Error: {e}'

    def get_single_category(self, id_category):
        try:
            result = self.categories.get_single_category(id_category)
            return result
        except pymysql.Error as e:
            return f'Error: {e}'

    def update_category(self, id_category, name):
        try:
            result = self.categories.update_category(id_category, name)
            return result
        except pymysql.Error as e:
            return f'Error: {e}'

    def delete_category(self, id_category):
        try:
            result = self.categories.delete_category(id_category)
            return result
        except pymysql.Error as e:
            return f'Error: {e}'
