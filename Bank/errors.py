# User
class InvalidUserData(Exception):
    def __init__(self, message = "Invalid user data", *args: object) -> None:
        super().__init__(message, *args)

class UserNotFound(Exception):
    def __init__(self, message = "User not found", *args: object) -> None:
        super().__init__(message, *args)

class UserAlreadyExists(Exception):
    def __init__(self, message = "User already exists", *args: object) -> None:
        super().__init__(message, *args)

class UserAlreadyOwnsAccount(Exception):
    def __init__(self, message = "User already owns account", *args: object) -> None:
        super().__init__(message, *args)

# Account
class AccountNotFound(Exception):
    def __init__(self, message = "Account not found", *args: object) -> None:
        super().__init__(message, *args)

class UnsufficientBalance(Exception):
    def __init__(self, message = "Unsufficient balance", *args: object) -> None:
        super().__init__(message, *args)

class InvalidAccountData(Exception):
    def __init__(self, message = "Invalid account data", *args: object) -> None:
        super().__init__(message, *args)

class InvalidAccountType(Exception):
    def __init__(self, message = "Invalid account type", *args: object) -> None:
        super().__init__(message, *args)

# Bank


# Menu
class InvalidMenuChoice(Exception):
    def __init__(self, message = "Invalid menu choice", *args: object) -> None:
        super().__init__(message, *args)
