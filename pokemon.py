from time import sleep
# import tqdm

class Pokemon:
    def __init__(self, name, level, type):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = 100
        self.current_health = self.max_health
        self.knocked_out = False

    def __repr__(self):
        return "{} is at level {} of type {} with current health {}.\n".format(
            self.name, self.level, self.type, self.current_health)

    def lose_health(self, damage):
        health_lost = damage
        self.current_health -= health_lost
        if self.current_health <= 0:
            self.is_knocked_out()
            self.knocked_out = True
        else:
            print(
                "{} has lost {} health. It now has {} health left.\n".format(self.name, health_lost,
                                                                             self.current_health))

    def gain_health(self, heal):
        if self.current_health <= 0:
            self.revive()
        health_gained = heal
        self.current_health += health_gained
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        print("{} has gained {} health. It now has {} health.\n".format(self.name, health_gained, self.current_health))

    def revive(self):
        if self.knocked_out:
            self.current_health = self.max_health
            print("{} was revived. It now has {} health.\n".format(self.name, self.current_health))

    def is_knocked_out(self):
        if self.current_health <= 0:
            print("{} has been knocked out.\n".format(self.name))

    def attack(self, other_pokemon):
        print("{} is attacking {}.\n".format(self.name, other_pokemon.name))
        if self.knocked_out:
            print("Cannot attack as Pokemon is knocked out.\n")
        elif self.type.lower() == other_pokemon.type.lower():
            print("{} attacked {} for {} damage.\n".format(self.name, other_pokemon.name, self.level))
            other_pokemon.lose_health(self.level)
        elif self.type.lower() == "fire":
            if other_pokemon.type.lower() == "grass":
                print("{} attacked {} for {} damage.\n".format(self.name, other_pokemon.name, self.level * 2))
                other_pokemon.lose_health(self.level * 2)
            elif other_pokemon.type.lower() == "water":
                print("{} attacked {} for {} damage.\n".format(self.name, other_pokemon.name, self.level * 0.5))
                other_pokemon.lose_health(self.level * 0.5)
        elif self.type.lower() == "grass":
            if other_pokemon.type.lower() == "fire":
                print("{} attacked {} for {} damage.\n".format(self.name, other_pokemon.name, self.level * 0.5))
                other_pokemon.lose_health(self.level * 0.5)
            elif other_pokemon.type.lower() == "water":
                print("{} attacked {} for {} damage.\n".format(self.name, other_pokemon.name, self.level * 2))
                other_pokemon.lose_health(self.level * 2)
        elif self.type.lower() == "water":
            if other_pokemon.type.lower() == "fire":
                print("{} attacked {} for {} damage.\n".format(self.name, other_pokemon.name, self.level * 2))
                other_pokemon.lose_health(self.level * 2)
            elif other_pokemon.type.lower() == "grass":
                print("{} attacked {} for {} damage.\n".format(self.name, other_pokemon.name, self.level * 0.5))
                other_pokemon.lose_health(self.level * 0.5)


class Trainer:
    def __init__(self, name, pokemons, potions, current_pokemon):
        self.name = name
        self.pokemons = pokemons
        self.potions = potions
        self.current_pokemon = current_pokemon

    def __repr__(self):
        return "{} has {} potions with {} currently active.\n".format(
            self.name, self.potions, self.current_pokemon.name)

    def use_potion(self):
        if self.potions > 0:
            if self.current_pokemon.current_health < self.current_pokemon.max_health:
                print("{} used a potion to heal {}.\n".format(self.name, self.current_pokemon.name))
                self.current_pokemon.gain_health(30)
                self.potions -= 1
                print("{} has {} potions left.\n".format(self.name, self.potions))
            else:
                print("Failed to use potion on {} as it is already at maximum health.\n".format(
                    self.current_pokemon.name))
        else:
            print("{} has no potions left.\n".format(self.name))

    def attack_other_trainer(self, other_pokemon):
        my_pokemon = self.current_pokemon
        opponent_pokemon = other_pokemon.current_pokemon
        my_pokemon.attack(opponent_pokemon)

    def switch_pokemon(self):

        # if pokemon.knocked_out:
            # print("Pokemon is knocked out. Cannot switch to specified Pokemon.\n")
            # return False

        for pokemon in self.pokemons:
            if not pokemon.knocked_out:
                self.current_pokemon = pokemon
                print("Switched pokemon to {}.\n".format(pokemon.name))
                return True
        return False


# Main Function Starts from here
# The game
# pikachu = Pokemon("Pikachu", 3, "Fire")
# bulbasaur = Pokemon("Bulbasaur", 3, "Grass")
# squirtle = Pokemon("Squirtle", 3, "Water")

# Trainer 1 Input
trainer1_name = input("Enter Your name: ")
trainer1_pokemons_no = int(input("Enter the number of pokemons you have: "))
trainer1_pokemons = []

for i in range(trainer1_pokemons_no):
    name = input("Enter the name of Pokemon no " + str(i + 1) + ": ")
    level = int(input("Enter the level of " + name + ": "))
    type = input("Enter the type of " + name + ": ")
    print()

    new_pokemon = Pokemon(name.title(), level, type)
    trainer1_pokemons.append(new_pokemon)

# trainer1_name = 'trainer1'
# trainer1_pokemons_no = 2
# trainer1_pokemons = []
# poke1 = Pokemon("poke1", 2, "Fire")
# trainer1_pokemons.append(poke1)
# poke2 = Pokemon("poke2", 3, "Water")
# trainer1_pokemons.append(poke2)
# trainer1_currently_active = trainer1_pokemons[0]

# trainer2_name = 'trainer2'
# trainer2_pokemons_no = 1
# trainer2_pokemons = []
# poke3 = Pokemon("poke3", 5, "Fire")
# trainer2_pokemons.append(poke3)
# trainer2_currently_active = trainer2_pokemons[0]


# #### trainer1_potions = 2
if trainer1_pokemons_no > 1:
    trainer1_pokemon_choice = input("Enter the pokemon you want to use: ")
    for i in trainer1_pokemons:
        if i.name == trainer1_pokemon_choice.title():
            trainer1_currently_active = i
else:
    trainer1_currently_active = trainer1_pokemons[0]

# # Trainer 2 Input
trainer2_name = input("Enter Your name: ")
trainer2_pokemons_no = int(input("Enter the number of pokemons you have: "))
trainer2_pokemons = []

for i in range(trainer2_pokemons_no):
    name = input("Enter the name of Pokemon no " + str(i + 1) + ": ")
    level = int(input("Enter the level of " + name + ": "))
    type = input("Enter the type of " + name + ": ")
    print()

    new_pokemon2 = Pokemon(name.title(), level, type)
    trainer2_pokemons.append(new_pokemon2)

# trainer2_potions = 2
if trainer2_pokemons_no > 1:
    trainer2_pokemon_choice = input("Enter the pokemon you want to use: ")
    for i in trainer2_pokemons:
        if i.name == trainer2_pokemon_choice.title():
            trainer2_currently_active = i
else:
    trainer2_currently_active = trainer2_pokemons[0]

print(trainer1_currently_active)
print(trainer2_currently_active)

trainer1 = Trainer(trainer1_name, trainer1_pokemons, 2, trainer1_currently_active)
trainer2 = Trainer(trainer2_name, trainer2_pokemons, 2, trainer2_currently_active)

# print(pikachu)
# print(bulbasaur)
# print(squirtle)

print(trainer1)
print(trainer2)

print("###########################################\n\n")
print("Game Starting...")

# trainer1.attack_other_trainer(trainer2)
# trainer2.attack_other_trainer(trainer1)
# trainer1.attack_other_trainer(trainer2)
# trainer2.use_potion()
# # trainer2.switch_pokemon(trainer2.pokemons[1])
# trainer1.attack_other_trainer(trainer2)
# trainer2.attack_other_trainer(trainer1)

while(1):
    trainer1.attack_other_trainer(trainer2)
    if trainer2.current_pokemon.knocked_out:
        if not trainer2.switch_pokemon():
            print(f"{trainer1.name} is winner")
            break
    sleep(1)
    trainer2.attack_other_trainer(trainer1)
    if trainer1.current_pokemon.knocked_out:
        if not trainer1.switch_pokemon():
            print(f"{trainer2.name} is winner")
            break