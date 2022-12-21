from errors_char import *

class Character:
    def __init__(self, names, sex, weapon, gameclass, otheriteam) -> None:
        self.names = []
        self.sex = sex
        self.gameclass = gameclass
        self.weapon = []
        self.otheriteam = []

    def print(self):
        return f"Character({self.names}, {self.sex},{self.gameclass}, {self.weapon}, {self.otheriteam})"

    def add_character(self, name):
        if name not in self.names:
            raise CharacterExists("Error: This name exist")
         self.names.append(self.names)

    def add_otheriteam(self, otheriteams):
        if otheriteams in self.otheriteam:
            raise InvalidCommand("Error: This iteam exist")

        self.otheriteam.append(self.otheriteam)

    def add_weapon(self, weapon):
         if weapon in self.weapons:
             raise InvalidCommand("Error: This weapon exist")

         self.weapon.append(weapon)
