class User:
    def __init__(self, f_name, l_name, email):
        self.first_name = f_name
        self.last_name = l_name
        self.email = email
        # self.is_rich = balance > 10000
    
    # def make_deposit(self, amount):
    #     self.balance += amount
    #     return self

    # def make_withdrawl(self, amount):
    #     if amount <= self.balance:
    #         self.balance -= amount
    #     else:
    #         print("You don't have enough money SUCKER!")
    #     return self

    # def show_balance(self):
    #     print(self.balance)
    #     return self


class BankAccount:
    bank_name = "Last Galactic Bank"
    all_accounts = []
    def __init__(self, balance, int_rate, user):
        self.balance = balance
        self.int_rate = int_rate
        self.user = user
        BankAccount.all_accounts.append(self)

    def __repr__(self):
        return f"{self.user.first_name}'s account"
        
jason = User("Jason", "Brady", "jbrady@codingdojo.com")
my_account= BankAccount(100, .002, jason)

print(my_account.user.email)
print(BankAccount.all_accounts)