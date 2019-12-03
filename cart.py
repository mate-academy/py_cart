"""Read the csv file and create instances of the Product class.
 Then add them to an instance of the Cart class and calculate total."""


class Product:
    """product object"""
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def calc_total(self):
        """calculate total product"""
        return self.price * self.qty

    def set_name(self, name):
        """set product name"""
        self.name = name


class Cart:
    """cart object"""
    def __init__(self, filename):
        self.items = []
        self.filename = filename
        with open(filename, 'rt') as csv_file:
            for row in csv_file.readlines():
                item = row.split(",")
                item_product = Product(item[0], float(item[1]), float(item[2]))
                self.items.append(item_product)

    def get_product(self, index):
        """return product for index"""
        return self.items[index]

    def calc_total(self):
        """calculate total products"""
        products_total = 0
        for i in self.items:
            products_total = i.calc_total() + products_total
        return products_total
