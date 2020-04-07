class Item:
    pass


class HealthPotion:
    def __init__(self, quantity=1):
        self.name = 'Health Potion'
        self.quantity = quantity
        self.heal_value = 3

    def __repr__(self):
        return f"{self.name}\nRestores 3 health!\nQuantity: {self.quantity}"
        pass

    def use_potion(self, pokemon):
        pokemon.gain_health(self.heal_value)
        self.quantity -= 1


class SuperPotion(HealthPotion):
    pass
