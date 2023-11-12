# ex2

class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Amount must be positive")
            return
        self.balance += amount

    def check_balance(self):
        print(f"Your current balance is {self.balance}")


class SavingsAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)
        self.interest = 0.01

    def set_interest(self, interest):
        self.interest = interest

    def calculate_interest(self):
        print(f"Your interest will be {self.balance * self.interest}")

    def withdrawal(self, amount):
        if self.balance - amount < 0:
            print("You don't have enough founds")
            return
        self.balance -= amount


class CheckingAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)

    def withdrawal(self, amount):
        if amount < 0:
            print("Amount must be positive")
            return
        self.balance -= amount


savings = SavingsAccount(100)
checking = CheckingAccount()

savings.deposit(10)
savings.check_balance()
savings.calculate_interest()

checking.deposit(10)
checking.withdrawal(5)
checking.check_balance()
