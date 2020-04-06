class Item:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity


class HealthPotion:
    def __init__(self, quantity):
        self.name = 'Health Potion'
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name}\nRestores 3 health!\nQuantity: {self.quantity}"


class SuperPotion(Item):
    pass
