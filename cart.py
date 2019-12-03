"""
Classes
-------
Product
Cart(Product)
"""
import csv


class Product:
    """
    Attributes
    ----------
    file_name : str
        name of the file which contains products
    volume : str
        all products from the file_name file
    num_of_prod : int
        number of the products

    Methods
    -------
    get_product(file_name)
    name() -- Return name of the product
    price() -- Return price of the product
    qty() -- Return quantity of the products
    """

    def __init__(self, file_name):
        self.file_name = file_name
        self.volume = None
        self.num_of_prod = None

    def get_product(self, list_order):
        """
        Read from the file_name file
        :param list_order: int
        :return: self
        """
        with open(self.file_name, 'r') as file:
            file_list = list(csv.reader(file))
            self.num_of_prod = len(file_list)
            self.volume = file_list[list_order]
            return self

    def name(self):
        """
        Return name of the product
        :return: str
        """
        name = 0
        return self.volume[name]

    def price(self):
        """
        Return price of the product
        :return: float
        """
        price = 1
        try:
            return float(self.volume[price])
        except ValueError:
            print('Expected floating point number for price value!')

    def qty(self):
        """
        Return quantity of the products
        :return: int
        """
        quantity = 2
        try:
            return int(self.volume[quantity])
        except ValueError:
            print('Expected an integer for quantity value!')


class Cart(Product):
    """
    Methods
    -------
    calv_total() -- Return total cost of all products
    """

    def calc_total(self):
        """
        Return total cost of all products
        :return: float
        """
        total = 0
        self.get_product(0)
        for idx in range(self.num_of_prod):
            self.get_product(idx)
            total += self.price() * self.qty()
        return total
