"""Product and Cart class realisation"""
import csv


class Product:
    """Product class"""
    def __init__(self, name, price, qty):
        self.name = name
        self.price = float(price)
        self.qty = int(qty)

    def __str__(self):
        return self.name

    def money_balance(self):
        """
        :return: price * balance(qty)
        """
        return self.price * self.qty


class Cart:
    """Product class"""
    def __init__(self, file):
        self.file = file

    def open_csv(self):
        """
        Open csv file
        :return: list
        """
        with open(self.file, 'rt') as csvfile:
            reader = list(csv.reader(csvfile, delimiter=','))
        return reader

    def get_product(self, index):
        """
        Create Product from csv file
        :param index: csv file line
        :return: instance class Product
        """
        reader = self.open_csv()
        product = Product(reader[index][0], reader[index][1], reader[index][2])
        return product

    def calc_total(self):
        """
        Count total price in all csv file
        :return: total price
        """
        reader = self.open_csv()
        result = 0
        for row in reader:
            result += float(row[1]) * float(row[2])
        return result
