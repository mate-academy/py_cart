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
    volume : list
        all products from the file_name file

    Methods
    -------
    name() -- Return name of the product
    price() -- Return price of the product
    qty() -- Return quantity of the products
    """

    def __init__(self):
        self.volume = []

    def name(self):
        """
        Return name of the product
        :return: str
        """
        name_index = 0
        return self.volume[name_index]

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
    Attributes
    ----------
    file_name : str
        name of the file which contains products
    products_amount : int
        number of the products
    Methods
    -------
    get_product(list_order) -- Read products from the file
    calv_total() -- Return total cost of all products
    """

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.get_product(0)
        self.products_amount = self.products_amount

    def get_product(self, list_order):
        """
        Read from the file_name file
        :param list_order: int
        :return: self
        """
        with open(self.file_name, 'r') as cart:
            products_list = list(csv.reader(cart))
            self.products_amount = len(products_list)
            self.volume = products_list[list_order]
            return self

    def calc_total(self):
        """
        Return total cost of all products
        :return: float
        """
        total = 0
        self.get_product(0)
        for idx in range(self.products_amount):
            self.get_product(idx)
            total += self.price() * self.qty()
        return total
