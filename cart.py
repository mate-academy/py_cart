"""
Classes
-------
Product
Cart(Product)
"""
import csv
import decimal


class Product:
    """
    Attributes
    ----------
    volume : list
        list of product name, price and quantity

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
        return float(self.volume[price])

    def qty(self):
        """
        Return quantity of the products
        :return: int
        """
        quantity = 2
        return self.volume[quantity]


class FileReader:
    """
    Read products from the file
    Attributes
    ----------
    file_name : str
        name of the file that contains products
    products_list : list
        list of all products
    products_amount : int
        number of the products

    Methods
    -------
    convert_price() -- convert price of the products to decimal value
    convert_qty() -- convert quantity of the products to integer value
    from string to numerical value
    """

    def __init__(self, file_name):
        self.file_name = file_name
        with open(self.file_name, 'r') as cart:
            self.products_list = list(csv.reader(cart))
            self.products_amount = len(self.products_list)
        self.convert_price()
        self.convert_qty()

    def convert_price(self):
        """Convert price of the products to decimal values"""
        price_idx = 1
        for product in self.products_list:
            try:
                product[price_idx] = decimal.Decimal(product[price_idx])
            except decimal.InvalidOperation:
                print('Expected decimal number for price value!')

    def convert_qty(self):
        """Convert quantity of the products to integer values"""
        qty_idx = 2
        for product in self.products_list:
            try:
                product[qty_idx] = int(product[qty_idx])
            except ValueError:
                print('Expected an integer for quantity value!')


class Cart(Product):
    """
    Attributes
    ----------
    file_name : str
        name of the file that contains products
    products_list : list
        list of all products

    Methods
    -------
    get_product(list_order) -- Read products from the file
    calc_total() -- Return total cost of all products
    """

    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self.products_list = FileReader(self.file_name).products_list

    def get_product(self, list_order):
        """
        Read from the file_name file
        :param list_order: int
        :return: self
        """
        self.volume = self.products_list[list_order]
        return self

    def calc_total(self):
        """
        Return total cost of all products
        :return: float
        """
        total = 0
        for idx in range(FileReader(self.file_name).products_amount):
            self.get_product(idx)
            total += self.price() * self.qty()
        return float(total)
