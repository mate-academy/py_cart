"""Read the csv file from task py_fcsv and create instances of the Product class.
Then add them to an instance of the Cart class and calculate total."""
import csv


class Product:
    """Class Product describes characteristics of the product"""
    def __init__(self, name: str, price: float, qty: int):
        self.name = name
        self.price = price
        self.qty = qty

    def get_name(self):
        """Returns name attribute"""
        return self.name

    def get_price(self):
        """Returns price attribute"""
        return self.price

    def get_qty(self):
        """Returns quantity"""
        return self.qty


class Cart:
    """Class Cart describes cart of the products"""
    def __init__(self, file_name):
        self.content = []
        with open(file_name, 'rt') as file:
            reader = csv.reader(file, delimiter=',')
            self.content = [Product(str(row[0]), float(row[1]), int(row[2])) for row in reader]
            print(self.content)

    def calc_total(self):
        """Returns total price of all products in the cart"""
        return sum([_.get_qty() * _.get_price() for _ in self.content])

    def get_product(self, index):
        """Returns product from the cart by index"""
        return self.content[index]
