'''
Module
'''


class Product:
    '''
    Info about Product
    '''
    def __init__(self, name, price, qty):
        '''

        :param name:
        :param price:
        :param qty:
        '''
        self.name = name
        self.price = price
        self.qty = qty

    def get_name(self):
        '''

        :return:
        '''
        return self.name

    def get_price(self):
        '''

        :return:
        '''
        return self.price

    def get_qty(self):
        '''

        :return:
        '''
        return self.qty


class Cart:
    '''
    Class cart
    '''
    def __init__(self, file_name):
        '''

        :param file_name:
        '''
        self.card_list = []
        with open(file_name, 'rt') as reading:
            for line in reading:
                line = line.split(',')
                product = Product(line[0], float(line[1]), int(line[2]))
                self.card_list.append(product)

    def get_product(self, index):
        '''

        :param index:
        :return:
        '''
        return self.card_list[index]

    def get_calc_total(self):
        '''

        :return:
        '''
        total = 0
        for i in self.card_list:
            total += i.get_price() * i.get_qty()
        return total
