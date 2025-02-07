import datetime

class item_class:
    def __init__(self, name, code, cost_price, sell_price, create_at, update_at):
        self.name = name
        self.code = code
        self.cost_price = cost_price
        self.sell_price = sell_price
        self.create_at = create_at
        self.update_at = update_at

    def update(self, name, code, cost_price, sell_price):
        self.name = name
        self.code = code
        self.cost_price = cost_price
        self.sell_price = sell_price
        self.update_at = datetime.now()    

    def __str__(self):
        return "Item(name={}, code={}, cost_price={}, sell_price={}, supplier={})".format(self.name, self.code, self.cost_price, self.sell_price)