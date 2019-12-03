"""The csv module implements classes to read and write tabular data in CSV format"""
import csv


class Product:
    """Product class"""
    def __init__(self, name, price, qty):
        self.name = name
        self.price = float(price)
        self.qty = float(qty)

    def get_total_price(self):
        """return total price of product"""
        return self.qty * self.price

    def get_price(self):
        """return price of product"""
        return self.price


class Cart:
    """Cart class"""
    def __init__(self, file):
        self._list_of_products = []
        with open(file, "rt") as products:
            for name, price, qty in csv.reader(products):
                self._list_of_products.append(Product(name, price, qty))

    def get_product(self, product_index):
        """return specified object from cart"""
        return self._list_of_products[product_index]

    def calc_total(self):
        """return total cost of products in cart"""
        return sum(product.get_total_price() for product in self._list_of_products)
