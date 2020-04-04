class Pokemon:
    def __init__(self, name, level, health, max_health, type, is_knocked_out):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.type = type
        self.is_knocked_out = is_knocked_out

    def __repr__(self):
        return self.name + "\nLevel " + str(self.level) + "\nHealth: " + str(self.health) + "/" + str(
            self.max_health) + "\nType: " + self.type + "\n"

    def lose_health(self, damage):
        if self.health - damage != 0:
            self.health -= damage
            print(self.name + ' lost ' + str(damage) + ' health.\n')
        else:
            self.knockout()

    def gain_health(self, healed):
        self.health += healed
        print('Your pokemon gained health: ' + healed + "\n")

    def knockout(self):
        self.is_knocked_out = True
        print('Your pokemon was knocked out!\n')

    def attack(self, pokemon_to_attack):
        print(self.name + " attacks " + pokemon_to_attack.name)
        if self.type == 'Fire' and pokemon_to_attack.type == 'Plant':
            pokemon_to_attack.lose_health(self.level * 2)
        elif self.type == 'Plant' and pokemon_to_attack.type == 'Fire':
            pokemon_to_attack.lose_health(self.level * (1 / 2))
        elif self.type == 'Water' and pokemon_to_attack.type == 'Fire':
            pokemon_to_attack.lose_health(self.level * 2)
        elif self.type == 'Water' and pokemon_to_attack.type == 'Plant':
            pokemon_to_attack.lose_health(self.level * (1 / 2))
        elif self.type == 'Plant' and pokemon_to_attack.type == 'Water':
            pokemon_to_attack.lose_health(self.level * 2)
        elif self.type == 'Fire' and pokemon_to_attack.type == 'Water':
            pokemon_to_attack.lose_health(self.level * (1 / 2))
        else:
            pokemon_to_attack.lose_heallth(self.level)


class Trainer:
    def __init__(self, name, potions, current_pokemon):
        self.name = name
        self.potions = potions
        self.current_pokemon = current_pokemon

    def __repr__(self):
        return self.name + "\nPotions: " + str(self.potions) + "\nActive Pokemon: " + str(self.current_pokemon)






squirtle = Pokemon('Squirtle', 1, 10, 10, 'Water', False)
bulbasaur = Pokemon('Bulbasaur', 1, 10, 10, 'Plant', False)
charmander = Pokemon('Charmander', 1, 10, 10, 'Fire', False)

#print(squirtle)
#squirtle.attack(bulbasaur)

#print(bulbasaur)

charmander.attack(bulbasaur)
charmander.attack(bulbasaur)
charmander.attack(bulbasaur)
charmander.attack(bulbasaur)
charmander.attack(bulbasaur)
charmander.attack(bulbasaur)

ash = Trainer('Ash Ketchum', 3, squirtle)
blake = Trainer('Blake the Trainer', 3, bulbasaur)
#print(ash)

#charmander.attack(bulbasaur)
#bulbasaur.attack(charmander)
#print(charmander)
#print(bulbasaur)
#print(squirtle)
#squirtle.attack(bulbasaur)
