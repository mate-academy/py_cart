"""The csv module implements classes to read and write tabular data in CSV format"""
import csv


class Product:
    """Product slass"""
    def __init__(self, name, price, qty):
        self.name = name
        self.price = float(price)
        self.qty = float(qty)
        self.cost = self.qty * self.price

    def get_total_cost(self):
        """return total cost of product"""
        return self.cost

    def get_price(self):
        """return price of product"""
        return self.price


class Cart:
    """Cart class"""
    def __init__(self, file):
        #  save data from csv in list
        self._values = []
        with open(file, "rt") as products:
            for line in csv.reader(products):
                self._values.append(line)

        #  create list of dictionaries with key from keys_list list and values from csv file
        self._keys_list = ["name", "price", "qty"]
        self._dict_list = []
        # cart.py:35:0: R1721: Unnecessary use of a comprehension (unnecessary-comprehension)
        # for value in self._values:
        #     self._dict_list.append({key: value for key, value in zip(self._keys_list, value)})
        for i in range(len(self._keys_list)):
            _dictionary = {}
            for j in range(len(self._values)):
                _dictionary[self._keys_list[j]] = self._values[i][j]
            self._dict_list.append(_dictionary)

        #  unpack dicts as keyword arguments and create list of instances of the Product class.
        self._objects = [Product(**dictionary) for dictionary in self._dict_list]

    def get_product(self, idx):
        """return specified object from cart"""
        return self._objects[idx]

    def calc_total(self):
        """return total cost of products in cart"""
        total = 0
        for i in range(len(self._objects)):
            total += self.get_product(i).cost
        return total
