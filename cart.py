"""Product and Cart class realisation"""
from csv import reader


class Product:
    """Product class"""
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

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
        self.product_list = []
        with open(file, 'rt') as csvfile:
            csv = list(reader(csvfile, delimiter=','))
            for name, price, qty in csv:
                product = Product(name, float(price), int(qty))
                self.product_list.append(product)

    def get_product(self, index):
        """
        Create Product from csv file
        :param index: csv file line
        :return: instance class Product
        """
        return self.product_list[index]

    def calc_total(self):
        """
        Count total price in all csv file
        :return: total price
        """
        result = 0
        for product in self.product_list:
            result += product.money_balance()
        return result
