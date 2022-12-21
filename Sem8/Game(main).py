from entities import Character
from errors_char import *


class Menu:
    def print_menu(self):
        print("1. Create a new character")
        print("2. Create a weapon for the existing character")
        print("3. Create a extra weapon for the existing character")
        print("4. Print all characters")
        print("5. Del existing character")

    def command_create_character(self, name, sex, gameclass):
        pass

    def run(self):
        # infinite menu loop
        while True:
            # print the menu
            self.print_menu()
            # ask the user to choose a command
            choice = input("Choose an item from the menu: \n> ")

            # catch errors
            try:
                # process the user's choice
                if choice == "1":
                    # ask the user to input the necessary command parameters
                    name = input("Enter the character name (alpha-numeric): ")
                    if name == int or name == float:
                        raise InvalidDataFormat("Invalid data")
                    sex = input("Enter the sex of the character: ")
                    gameclass = input("Enter the class of the character:")
                    weapon = input("Enter a weapon:")
                    otheriteam = input("Enter a extra weapon: ")
                    Character.add_character(name, sex, gameclass, weapon, otheriteam)

                elif choice == "2":
                    weapon = input("Enter a weapon:")
                    name = input("Enter the character name: ")
                    if name in Character.add_character:
                        raise CharacterExists("Character exists")
                    Character.add_weapon(name, weapon)

                elif choice == "3":
                    name = input("Enter the character name: ")
                    if name in Character.add_character:
                        raise CharacterExists("Character exists")
                    otheriteam = input("Enter a extra weapon: ")
                    Character.add_otheriteam(name, otheriteam)

                elif choice == "4":
                    for k in Character.names:
                        print(k.print())

                elif choice == "5":
                    for k in Character.names:
                        del Character.names[k]
                else:
                    raise InvalidCommand("Error: Invalid choice")
            except Exception as ex:
                print(f"Error: {str(ex)}")

            print()


if __name__ == '__main__':
    menu = Menu()
    menu.run()
