'''
    A shop
'''

class Shop():
    def __init__(self, items):
        self.items = items

class ShopEntry():
    def __init__(self, name, price):
        self.name = name,
        print name
        self.price = price

    def db(self):
        print('Item: {}, {} credits'.format(self.name[0], self.price))

def grab():
    # Context is now in the shop
    pass


apples = ShopEntry('apple', '.40')
pear = ShopEntry('pear', '.60')

apples.db()
pear.db()
