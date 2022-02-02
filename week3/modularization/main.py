from User import User

steve_data = { "name": "Steve Winmore", "email": "stevew1nz@gmail.com", "nickname": "The Stevinator", "new_user": True, "height": "Very Tall", "account": 3, "int_rate": 0.02, "balance": 250}
steve = User(steve_data)

steve.make_deposit(100)
steve.check_balance()
