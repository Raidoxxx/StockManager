from manager.item import item_class
from typing import List

class supplier_class:

    all_items = []
    def __init__(self, name, id, items: List[item_class]):
        self.name = name
        self.id = id
        self.items = items
        self.load_items()
    def __str__(self):
        return "Supplier(name={}, id={}, items={})".format(self.name, self.id, self.items)
    def load_items(self):
        for item in self.items:
            self.all_items.append(item)

    def get_all_items(self):
        return self.all_items