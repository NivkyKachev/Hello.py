import random


class MissingParameterError(Exception):
    pass


class InvalidParameterError(Exception):
    def __init__(self, invalid_parameter, *args):
        message = f"Invalid class parameter: {invalid_parameter}"
        super().__init__(message, *args)


class InvalidAgeError(InvalidParameterError):
    def __init__(self):
        super().__init__("age")


class InvalidSoundError(InvalidParameterError):
    def __init__(self):
        super().__init__("sound")


class JungleAnimal:
    def __init__(self, name, age, sound):
        if type(name) != str:
            raise InvalidParameterError('name')
        elif type(age) != int:
            raise InvalidAgeError()
        elif type(sound) != str:
            raise InvalidSoundError()
        elif 'name' not in name:
            raise MissingParameterError(":'(")
        elif 'age' not in age:
            raise MissingParameterError()
        elif 'sound' not in sound:
            raise MissingParameterError()
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print({self.name} + "says" + {self.sound} + "!")

    def print(self):
        pass

    def daily_task(self):
        pass


class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 15:
            raise InvalidAgeError()
        elif sound.count("r") <= 1:
            raise InvalidSoundError()

    def print(self):
        print(f"Jaguar(+ {self.name}, {self.age}, {self.sound} +)")

    def daily_task(self, animals):
        for i in range(len(animals)):
            if type(animals[i]) == Lemur or type(animals[i]) == Human:
                del animals[i]
                print(f"The Jaguar hunted down {self.name} the {self.__name__}")


class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError()
        elif "e" not in sound:
            raise InvalidSoundError()

    def print(self):
        print(f"Lemur(+ {self.name}, {self.age}, {self.sound} +)")

    def daily_task(self, fruits):
        if fruits >= 10:
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            fruits = fruits - 10
            return fruits
        elif fruits < 10:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
            return 0
        elif fruits <= 0:
            print(f"{self.name} the Lemur couldn't find anything to eat")
            self.make_sound()
            self.make_sound()
            return 0


class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError()
        elif "e" not in sound:
            raise InvalidSoundError()

    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals, building):
        element = animals.index(self)
        if element == 0 and type(animals[element + 1]) == Human:
            buildings.append(Building("A new object of type building"))
        elif element == len(animals) - 1 and type(animals[element - 1]) == Human:
            buildings.append(Building("A new object of type building"))
        elif type(animals[element - 1]) == Human and type(animals[element + 1]) == Human:
            buildings.append(Building("A new object of type building"))


class Building:
    def __init__(self, type):
        self.type = type


fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

for i in range(102):
    random_number = random.randint(0, 9)
    random_name = names[random.randint(0, len(names) - 1)]
    random_age = random.randint(7, 20)
    random_sound = sounds[random.randint(0, len(sounds) - 1)]

    try:
        if 0 <= random_number <= 3:
            animals.append(Lemur(random_name, random_age, random_sound))
        elif 4 <= random_number <= 7:
            animals.append(Jaguar(random_name, random_age, random_sound))
        elif 8 <= random_number <= 9:
            animals.append(Human(random_name, random_age, random_sound))
    except Exception as e:
        print(random_number, random_name, random_age, random_sound, str(e))

print(f"The jungle now has {len(animals)} animals")

for anim in animals:
    if type(anim) == Jaguar:
        anim.daily_task(animals)
    elif type(anim) == Lemur:
        fruits = anim.daily_task(fruits)
    elif type(anim) == Human:
        anim.daily_task(animals, buildings)

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)
