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

    def pie(self):
        """
        Return amount of pies from given
        qty of fruits
        :return:
        """
        return self.qty / 2

    def juice(self):
        """
        Return amount of juice glasses from given
        qty of fruits
        :return:
        """
        return self.qty / 5


class Cart:
    """
    cart docstring
    """
    def __init__(self, csv_name):
        """

        :param csv_name:
        """
        self.csv_name = csv_name
        with open(self.csv_name, 'rt') as file:
            self.csv = [line.split(',') for line in file.readlines()]

    def calc_total(self):
        """

        :return:
        """
        return sum(float(line[1]) * int(line[2]) for line in self.csv)

    def get_product(self, param):
        """

        :param param:
        :return:
        """
        return Product(self.csv[param][0], float(self.csv[param][1]), int(self.csv[param][2]))
