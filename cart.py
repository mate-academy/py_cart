"""
Read the csv file from task [py_fcsv](https://github.com/mate-academy/py_fcsv)
and create instances of the Product class. Then add them to an instance of the
Cart class and calculate total.
"""

from csv import reader
from functools import reduce


class Product:
    """
    class product
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty


class Cart:
    """
    class cart
    """

    def __init__(self, filename):
        self.filename = filename

    def get_product(self, index: int) -> Product:
        """
        Return product from csv file by using index parameter.
        :param index: int
        :return: Product
        """
        with open(self.filename, 'rt') as file:
            csv_reader = list(reader(file, delimiter=','))
            prod_param_lst = csv_reader[index]
            product = Product(
                prod_param_lst[0],
                float(prod_param_lst[1]),
                float(prod_param_lst[2])
            )
            return product

    def calc_total(self) -> float:
        """
        There is a CSV file containing data in this format:
        Product name, price, quantity
        Calculate total cost for all products (price * quantity).
        :return: float
        """
        with open(self.filename, 'rt') as file:
            sum_prod_costs = 0.0
            csv_reader = reader(file, delimiter=',')
            param_lsts = [list(map(float, line[1:])) for line in csv_reader]
            for lst in param_lsts:
                sum_prod_costs += reduce((lambda x, y: x * y), lst)
        return sum_prod_costs
