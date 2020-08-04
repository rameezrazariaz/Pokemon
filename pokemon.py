class Pokemon:
    def __init__(self, name, level, type, knocked_out):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = 100
        self.current_health = self.max_health
        self.knocked_out = knocked_out

    def __repr__(self):
        return "{} is at level {} of type {} with current health {}.\n".format(
            self.name, self.level, self.type, self.current_health)

    def lose_health(self, damage):
        health_lost = damage
        self.current_health -= health_lost
        if self.current_health <= 0:
            self.is_knocked_out()
        else:
            print(
                "{} has lost {} health. It now has {} health left.\n".format(self.name, health_lost, self.current_health))

    def gain_health(self, heal):
        if self.current_health <= 0:
            self.revive()
        health_gained = heal
        self.current_health += health_gained
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        print("{} has gained {} health. It now has {} health.\n".format(self.name, health_gained, self.current_health))

    def revive(self):
        if not self.knocked_out:
            self.current_health = self.max_health
            print("{} was revived. It now has {} health.\n".format(self.name, self.current_health))

    def is_knocked_out(self):
        if self.current_health <= 0:
            print("{} has been knocked out.\n".format(self.name))

    def attack(self, other_pokemon):
        print("{} is attacking {}.\n".format(self.name, other_pokemon.name))
        if self.knocked_out:
            print("Cannot attack as Pokemon is knocked out.\n")
        elif self.type == "Fire":
            if other_pokemon.type == "Grass":
                print("{} attacked {} for {} damage.\n".format(self.name, other_pokemon.name, self.level * 2))
                other_pokemon.lose_health(self.level * 2)
            elif other_pokemon.type == "Water":
                print("{} attacked {} for {} damage.\n".format(self.name, other_pokemon.name, self.level * 0.5))
                other_pokemon.lose_health(self.level * 0.5)
        elif self.type == "Grass":
            if other_pokemon.type == "Fire":
                print("{} attacked {} for {} damage.\n".format(self.name, other_pokemon.name, self.level * 0.5))
                other_pokemon.lose_health(self.level * 0.5)
            elif other_pokemon.type == "Water":
                print("{} attacked {} for {} damage.\n".format(self.name, other_pokemon.name, self.level * 2))
                other_pokemon.lose_health(self.level * 2)
        elif self.type == "Water":
            if other_pokemon.type == "Fire":
                print("{} attacked {} for {} damage.\n".format(self.name, other_pokemon.name, self.level * 2))
                other_pokemon.lose_health(self.level * 2)
            elif other_pokemon.type == "Grass":
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
                print("Failed to use potion on {} as it is already at maximum health.\n".format(self.current_pokemon.name))
        else:
            print("{} has no potions left.\n".format(self.name))

    def attack_other_trainer(self, other_pokemon):
        my_pokemon = self.current_pokemon
        opponent_pokemon = other_pokemon.current_pokemon
        my_pokemon.attack(opponent_pokemon)

    def switch_pokemon(self, pokemon):
        if self.pokemons[pokemon].knocked_out:
            print("Pokemon is knocked out. Cannot switch to specified Pokemon.\n")
        else:
            self.current_pokemon = pokemon
            print("Switched pokemon to {}.\n".format(self.pokemons[pokemon].name))


# The game
pikachu = Pokemon("Pikachu", 3, "Fire", False)
bulbasaur = Pokemon("Bulbasaur", 3, "Grass", False)
squirtle = Pokemon("Squirtle", 3, "Water", False)

trainer1 = Trainer('Trainer1', [pikachu], 2, pikachu)
trainer2 = Trainer('Trainer2', [bulbasaur, squirtle], 2, bulbasaur)

print(pikachu)
print(bulbasaur)
print(squirtle)

print(trainer1)
print(trainer2)


trainer1.attack_other_trainer(trainer2)
trainer2.attack_other_trainer(trainer1)
trainer2.use_potion()
trainer1.attack_other_trainer(trainer2)
trainer2.switch_pokemon(0)
trainer2.switch_pokemon(1)
