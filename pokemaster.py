import items
from items import *


class Pokemon:
    def __init__(self, name, level, health, max_health, pokemon_type, is_knocked_out):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = max_health
        self.pokemon_type = pokemon_type
        self.is_knocked_out = is_knocked_out
        self.experience = 0
        self.experience_needed = level * 10

    def __repr__(self):
        return f"{self.name}\nLevel {self.level}\nHealth: {self.health}/{self.max_health}\nType: {self.pokemon_type}\nExperience: {self.experience}/{self.experience_needed} "

    def lose_health(self, damage):
        if self.health - damage <= 0:
            self.health -= damage
            print(f"{self.name} lost {damage} health.\n")
        else:
            self.knockout()

    def gain_health(self, health_to_be_gained):
        self.health += health_to_be_gained
        print(f'{self.name} gained {health_to_be_gained} health!')
        print(f'{self.name} now has {self.health} health.\n')

    def knockout(self):
        self.health = 0
        self.is_knocked_out = True
        print('Knockout!\n')

    def calculate_damage(self, pokemon_to_attack):
        if self.pokemon_type == 'Fire' and pokemon_to_attack.pokemon_type == 'Grass':
            return self.level * 2
        elif self.pokemon_type == 'Fire' and pokemon_to_attack.pokemon_type == 'Water':
            return self.level * (1 / 2)
        elif self.pokemon_type == 'Grass' and pokemon_to_attack.pokemon_type == 'Fire':
            return self.level * (1 / 2)
        elif self.pokemon_type == 'Grass' and pokemon_to_attack.pokemon_type == 'Water':
            return self.level * 2
        elif self.pokemon_type == 'Water' and pokemon_to_attack.pokemon_type == 'Fire':
            return self.level * 2
        elif self.pokemon_type == 'Water' and pokemon_to_attack.pokemon_type == 'Grass':
            return self.level * (1 / 2)
        else:
            return self.level

    def attack(self, pokemon_to_attack):
        print(f"{self.name} attacks {pokemon_to_attack.name}!")
        calculated_damage = self.calculate_damage(pokemon_to_attack)
        pokemon_to_attack.lose_health(calculated_damage)
        if pokemon_to_attack.is_knocked_out:
            self.gain_experience(pokemon_to_attack.level)

    def gain_experience(self, experience_gained):
        self.experience += experience_gained
        print(f"{self.name} gained {experience_gained} experience\n")
        if self.experience >= self.experience_needed:
            self.level_up()

    def level_up(self):
        print(f'{self.name} leveled up!')
        self.level += 1
        self.max_health += 5
        self.health += 5
        self.experience = 0
        self.experience_needed += 5


class Trainer:
    def __init__(self, name, potions, current_pokemon, bench=None):
        self.name = name
        self.potions = potions
        self.current_pokemon = current_pokemon
        self.bench = bench
        self.inventory = []

    def __repr__(self):
        return f"{self.name}\nPotions: {self.potions} \nActive Pokemon: {self.current_pokemon.name} \nBench: {self.bench}\n"

    def add_to_inventory(self, new_item):
        if new_item not in self.inventory:
            self.inventory.append(new_item)
            print(f'{new_item.name} added to inventory!\n')
        else:
            pass
#work here
    def use_item(self, item_to_use):
        #if items.item_to_use in self.inventory:
        print(item_to_use)
        print("so far")

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


squirtle = Pokemon('Squirtle', 2, 10, 10, 'Water', False)
bulbasaur = Pokemon('Bulbasaur', 2, 10, 10, 'Grass', False)
charmander = Pokemon('Charmander', 2, 10, 10, 'Fire', False)
eevee = Pokemon('Eevee', 1, 10, 10, 'Normal', False)
squirtle2 = Pokemon('Squirtle', 1, 10, 10, 'Water', False)

bulbasaur.experience = 9
# print(bulbasaur.experience)


ash_bench = [eevee, charmander]
blake_bench = [squirtle2]

ash = Trainer('Ash Ketchum', 3, squirtle, bench=ash_bench)
blake = Trainer('Blake the Trainer', 3, bulbasaur, blake_bench)
ash.add_to_inventory(HealthPotion())

print(ash.inventory)
ash.use_item(HealthPotion)
print(ash.inventory)
# print(ash.bench)

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
# print(bulbasaur)
# print(squirtle)
# blake.attack_trainer(ash)
# print(blake)
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
