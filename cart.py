"""
Product
"""


class Product:
    """
    Product
    """
    def __init__(self, data):
        self._name = data["name"]
        self._price = float(data["price"])
        self._qty = float(data["qty"])

    @property
    def name(self):
        """
        name
        """
        return self._name

    @property
    def price(self):
        """
        price
        """
        return self._price

    @property
    def qty(self):
        """
        qty
        """
        return self._qty


class Cart:
    """
    Cart
    """
    def __init__(self, file):
        with open(file, 'rt') as file1:
            self._data = []
            for line in file1:
                product_info = line.split(',')
                new_product = {
                    "name": product_info[0],
                    "price": product_info[1],
                    "qty": product_info[2],
                }
                self._data.append(Product(new_product))

    def get_product(self, index):
        """
        product
        """
        return self._data[index]

    def calc_total(self):
        """
        total
        """
        return sum([data.price * data.qty for data in self._data])
