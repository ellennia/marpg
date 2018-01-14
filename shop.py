'''
    A shop
'''

class Shop():
    def __init__(self, items):
        self.items = items

class ShopEntry():
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def db(self):
        print('Item: {}, {} credits'.format(self.name, self.price))

def grab():
    # Context is now in the shop
    pass


apples = ShopEntry('apple', 'delicious red fruit', '.40')
pear = ShopEntry('pear', 'less delicious green fruit', '.60')

apples.db()
pear.db()
