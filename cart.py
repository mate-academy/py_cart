"""Module to make calculations based on reports"""
import csv


class Product:
    """Product item, its name, price and quantity"""
    def __init__(self, name, price, qty):
        self.name = name
        self.price = float(price)
        self.qty = float(qty)

    def get_total_sum(self):
        """Return total sum"""
        return self.price * self.qty

    def get_price(self):
        """Return price of product"""
        return self.price


class Cart:
    """Cart of products"""
    def __init__(self, filename):
        self._filename = filename
        self._products = []
        """Open and read report"""
        with open(self._filename) as reader:
            products_data = csv.reader(reader, delimiter=',')
            for i in products_data:
                self._products.append(Product(i[0], i[1], i[2]))

    def get_product(self, index):
        """Return product by index"""
        try:
            return self._products[index]
        except IndexError:
            print('There are only {0}'.format(str(len(self._products))))

    def calc_total(self):
        """Return total sum of all products"""
        total = 0
        for i in self._products:
            total += i.get_total_sum()
        return total
