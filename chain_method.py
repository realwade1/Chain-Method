class User:		# declare a class and give it name User
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0.00
    
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print('User: ' + self.name + ',Balance: $' + str(self.account_balance))
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

jordan = User("Jay Wade", "email@email.com")
matthew = User("Matthew Wade", "mat@email.com")
oliver = User("Oliver Wade", "oli@email.com")

jordan.make_deposit(100).make_deposit(200).make_deposit(300).display_user_balance()

matthew.make_deposit(25).make_deposit(35).make_withdrawal(30).make_withdrawal(40).display_user_balance()

oliver.make_deposit(25000).make_withdrawal(500).make_withdrawal(1500).make_withdrawal(3500).display_user_balance()

jordan.transfer_money(oliver, 200).display_user_balance()
oliver.display_user_balance()