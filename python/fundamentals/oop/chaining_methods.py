class User:
    def __init__(self, name):
        self.name = name
        self.user_balance = 0
    
    def make_deposit(self, amount):
        self.user_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.user_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f'User: {self.name}, Balance: ${self.user_balance}')
        return self
    
    def transfer_money(self, other_user, amount):
        self.user_balance -= amount
        other_user.user_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()

guido = User("Guido van Rossum")
bill = User("Bill Gates")
zuck = User("Mark Zuckerberg")

guido.make_deposit(10000).make_deposit(20000).make_deposit(30000).make_withdrawal(150).display_user_balance()

bill.make_deposit(10000).make_deposit(30000).make_withdrawal(4000).make_withdrawal(3500).display_user_balance()

zuck.make_deposit(100000).make_withdrawal(30000).make_withdrawal(25000).make_withdrawal(14550).display_user_balance()

guido.transfer_money(zuck, 10000)