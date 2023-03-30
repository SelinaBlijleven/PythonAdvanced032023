class BankAccount:

    def __init__(self, holder, balance):
        self.__holder = holder
        self.__balance = balance

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def info(self):
        return f"Deze bankaccount is van {self.__holder} en bevat {self.__balance} euro."