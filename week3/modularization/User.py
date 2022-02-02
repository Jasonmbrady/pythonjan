from Account import BankAccount

class User:
    def __init__(self, data):
        self.name = data["name"]
        self.email = data["email"]
        self.account = BankAccount(data)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def check_balance(self):
        balance = self.account.balance
        print(f"{self.name}'s balance is: {balance}")

class Referral:
    pass