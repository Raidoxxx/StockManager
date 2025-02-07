from manager.supplier import supplier_class

class stock_class:

    suppliers = []

    def __init__(self, suppliers: list[supplier_class]):
        self.suppliers = suppliers

    def __str__(self):
        for supplier in self.suppliers:
            text = "Supplier: {}\n".format(supplier.name)
            for item in supplier.items:
                text += "Item: name={}, code={}, cost_price={}, sell_price={}\n".format(item.name, item.code, item.cost_price, item.sell_price)
            print(text)