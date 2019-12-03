"""
Read the csv file from task [py_fcsv](https://github.com/mate-academy/py_fcsv)
and create instances of the Product class. Then add them to an instance of the
Cart class and calculate total.
"""

from csv import reader


class Product:
    """
    class product
    """

    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_qty(self):
        return self.qty


class Cart:
    """
    class cart
    """

    def __init__(self, filename):
        self.cart_lst = []

        with open(filename, 'rt') as file:
            product_lsts = list(reader(file, delimiter=','))
            for product_lst in product_lsts:
                product = Product(
                    product_lst[0],
                    float(product_lst[1]),
                    float(product_lst[2])
                )
                self.cart_lst.append(product)

    def get_product(self, index: int) -> Product:
        """
        Return product from csv file by using index parameter.
        :param index: int
        :return: Product
        """
        return self.cart_lst[index]

    def calc_total(self) -> float:
        """
        There is a CSV file containing data in this format:
        Product name, price, quantity
        Calculate total cost for all products (price * quantity).
        :return: float
        """
        total_sum = 0
        for product in self.cart_lst:
            total_sum += product.get_price() * product.get_qty()
        return total_sum
