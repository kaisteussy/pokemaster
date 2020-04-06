import items


class Pokemon:
    def __init__(self, name, level, health, max_health, pokemon_type, is_knocked_out):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.pokemon_type = pokemon_type
        self.is_knocked_out = is_knocked_out

    def __repr__(self):
        return self.name + "\nLevel " + str(self.level) + "\nHealth: " + str(self.health) + "/" + str(
            self.max_health) + "\nType: " + self.pokemon_type + "\n"

    def lose_health(self, damage):
        if self.health - damage != 0:
            self.health -= damage
            print(self.name + ' lost ' + str(damage) + ' health.\n')
        else:
            self.knockout()

    def gain_health(self, potion):
        self.health += potion
        print('Your pokemon gained health: ' + str(potion) + "\n")

    def knockout(self):
        self.health = 0
        self.is_knocked_out = True
        print('Knockout!\n')

    def attack(self, pokemon_to_attack):
        print(self.name + " attacks " + pokemon_to_attack.name + "!")
        if self.pokemon_type == 'Fire' and pokemon_to_attack.pokemon_type == 'Grass':
            pokemon_to_attack.lose_health(self.level * 2)
        elif self.pokemon_type == 'Grass' and pokemon_to_attack.pokemon_type == 'Fire':
            pokemon_to_attack.lose_health(self.level * (1 / 2))
        elif self.pokemon_type == 'Water' and pokemon_to_attack.pokemon_type == 'Fire':
            pokemon_to_attack.lose_health(self.level * 2)
        elif self.pokemon_type == 'Water' and pokemon_to_attack.pokemon_type == 'Grass':
            pokemon_to_attack.lose_health(self.level * (1 / 2))
        elif self.pokemon_type == 'Grass' and pokemon_to_attack.pokemon_type == 'Water':
            pokemon_to_attack.lose_health(self.level * 2)
        elif self.pokemon_type == 'Fire' and pokemon_to_attack.pokemon_type == 'Water':
            pokemon_to_attack.lose_health(self.level * (1 / 2))
        else:
            pokemon_to_attack.lose_health(self.level)


class Trainer:
    def __init__(self, name, potions, current_pokemon, bench=None, inventory=None):
        self.name = name
        self.potions = potions
        self.current_pokemon = current_pokemon
        self.bench = bench
        self.inventory = inventory

    def __repr__(self):
        return f"{self.name}\nPotions: {self.potions} \nActive Pokemon: {self.current_pokemon} \nBench: {self.bench}\n"

    def add_to_inventory(self, *new_item):
        print('Item added to inventory!')
        self.inventory.append(new_item)

    def use_potion(self):
        print("Using potion on " + self.current_pokemon.name + "...")
        if self.current_pokemon.health == 0:
            print(self.current_pokemon.name + " is knocked out! You can't use that.\n")
        else:
            self.current_pokemon.gain_health(3)

    def switch_pokemon(self, new_pokemon):
        print(self.name + " is switching pokemon...")
        if self.bench is None:
            print("Your bench is empty!\n")
        elif new_pokemon not in self.bench:
            print("That pokemon is not on your bench!\n")
        elif new_pokemon != self.current_pokemon:
            self.bench.append(self.current_pokemon)
            self.bench.remove(new_pokemon)
            self.current_pokemon = new_pokemon
            print("Go " + self.current_pokemon.name + "!\n")
        else:
            print("That pokemon is already active!\n")

    def attack_trainer(self, trainer_to_attack):
        if self.current_pokemon.is_knocked_out:
            print(self.current_pokemon.name + " is knocked out, switch it out or retreat!\n")
        # potential for removal if not possible
        elif trainer_to_attack.current_pokemon.is_knocked_out:
            print("That pokemon is already knocked out!\n")
        else:
            self.current_pokemon.attack(trainer_to_attack.current_pokemon)


squirtle = Pokemon('Squirtle', 1, 10, 10, 'Water', False)
bulbasaur = Pokemon('Bulbasaur', 1, 10, 10, 'Grass', False)
charmander = Pokemon('Charmander', 1, 10, 10, 'Fire', False)
eevee = Pokemon('Eevee', 1, 10, 10, 'Normal', False)
squirtle2 = Pokemon('Squirtle', 1, 10, 10, 'Water', False)

health_potion = items.HealthPotion(2)
#super_potion = items.Item('Super Potion', 1)


ash_bench = [eevee, charmander]
blake_bench = [squirtle2]

ash = Trainer('Ash Ketchum', 3, squirtle, bench=ash_bench, inventory=[])
blake = Trainer('Blake the Trainer', 3, bulbasaur, blake_bench)
ash.add_to_inventory(health_potion)

print(ash.inventory)
print(ash.bench)

# print(ash)
# ash.switch_pokemon(eevee)
# print(ash)
#
# print(blake)
# blake.switch_pokemon(squirtle2)
# print(blake)

# blake.attack_trainer(ash)
# blake.attack_trainer(ash)
# blake.attack_trainer(ash)
# blake.attack_trainer(ash)
# blake.attack_trainer(ash)
# blake.attack_trainer(ash)
# ash.switch_pokemon(charmander)
# ash.switch_pokemon(charmander)
# ash.attack_trainer(blake)
# ash.attack_trainer(blake)
# ash.attack_trainer(blake)
# ash.attack_trainer(blake)
# ash.attack_trainer(blake)
# blake.switch_pokemon(squirtle)
# blake.attack_trainer(ash)
# blake.use_potion()

# print(ash.current_pokemon.health)


# print(squirtle)
# squirtle.attack(bulbasaur)

# print(bulbasaur)

# print(ash)
# print(blake.current_pokemon)
# blake.use_potion()
