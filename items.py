class Potion:
    def __init__(self, name, heal_value):
        self.name = name
        self.heal_value = heal_value

    # def use(self):
    #     pass


class HealthPotion:
    def __init__(self, name="Health Potion", heal_value=3):
        #self.trainer = trainer
        self.name = name
        self.heal_value = heal_value

    def __repr__(self):
        return self.name

    # def use(self):
    #     return self.heal_value
