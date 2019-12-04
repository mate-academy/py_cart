"""
docstring
"""


class Product:
    """
    Product docstring
    """

    def __init__(self, name, price, qty):
        """

        :param name:
        :param price:
        :param qty:
        """
        self.name = name
        self.price = price
        self.qty = qty

    def get_name(self):
        """
        Return products name
        :return:
        """
        return self.name

    def get_qty(self):
        """
        return products qty
        :return:
        """
        return self.qty


class Cart:
    """
    cart docstring
    """
    def __init__(self, csv_name):
        """

        :param csv_name:
        """
        self.csv_name = csv_name
        self.prod_list = []
        with open(self.csv_name, 'rt') as file:
            self.csv = [line.split(',') for line in file.readlines()]
            for name, price, qty in self.csv:
                self.prod_list.append(Product(name, float(price), int(qty)))
            self.total = sum(float(line[1]) * int(line[2]) for line in self.csv)

    def calc_total(self):
        """
        total
        :return:
        """
        return self.total

    def get_product(self, param):
        """

        :param param:
        :return:
        """
        return self.prod_list[param]
