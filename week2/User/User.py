class User:
    user_id = 0
    def __init__(self, f_name, l_name, balance, email):
        self.first_name = f_name
        self.last_name = l_name
        self.balance = balance
        self.email = email
        self.is_rich = balance > 10000
    
    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawl(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("You don't have enough money SUCKER!")
        return self

    def show_balance(self):
        print(self.balance)
        return self

    @classmethod
    def change_user_id(cls, new_id):
         cls.user_id = new_id

jason = User("Jason", "Brady", .02, "jbrady@codingdojo.com")
jason.make_deposit(100).make_withdrawl(20).show_balance()
