class InvalidCommand(Exception):
    def __init__(self, message = "Invalid command", *args: object) -> None:
        super().__init__(message, *args)

class CharacterNotFound(Exception):
    def __init__(self, message = "Character not found", *args: object) -> None:
        super().__init__(message, *args)

class InvalidCharacterClass(Exception):
    def __init__(self, message = "Invalid character class", *args: object) -> None:
        super().__init__(message, *args)

class CharacterExists(Exception):
    def __init__(self, message = "Character exists", *args: object) -> None:
        super().__init__(message, *args)

class InvalidDataFormat(Exception):
    def __init__(self, message = "Invalid data format", *args: object) -> None:
        super().__init__(message, *args)
