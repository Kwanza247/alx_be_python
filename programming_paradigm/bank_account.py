class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance #encapsulated attribute

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance +=amount

    def withdraw(self, amount):
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")