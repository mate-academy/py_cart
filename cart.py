"""
Read the csv file from task [py_fcsv](https://github.com/mate-academy/py_fcsv)
and create instances of the Product class.
Then add them to an instance of the Cart class and calculate total.
"""


import csv


class Product:
    """Class Product"""
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def get_cost(self):
        """Get cost of all products"""
        return self.price * self.qty

    def get_name(self):
        """Get name"""
        return self.name


class Cart:
    """Class Cart"""
    def __init__(self, file_name):
        self.file_name = file_name
        self.card_list = []
        with open(file_name, 'rt') as rfile:
            reader = csv.reader(rfile)
            for line in reader:
                product = Product(line[0], float(line[1]), int(line[2]))
                self.card_list.append(product)

    def get_product(self, num):
        """Get product"""
        return self.card_list[num]

    def calc_total(self):
        """Get total"""
        total = []
        for i in self.card_list:
            total.append(i.get_cost())
        return sum(total)
