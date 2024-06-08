class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number  # Private variable
        self.__balance = initial_balance        # Private variable

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        else:
            return "Deposit amount must be positive."

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance: {self.__balance}"
        else:
            return "Insufficient balance or invalid amount."

    # Public method to get the current balance
    def get_balance(self):
        return f"Current balance: {self.__balance}"

    # Public method to get the account number
    def get_account_number(self):
        return f"Account number: {self.__account_number}"

# Create an instance of BankAccount
account = BankAccount("123456789", 1000)

# Access public methods
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())

# Attempting to access private variables from outside the class will result in an AttributeError
try:
    print(account.__balance)
except AttributeError:
    print("Cannot access private variable __balance")

# Accessing private variables using name mangling
print(account._BankAccount__balance)  # This is not recommended as it breaks encapsulation
