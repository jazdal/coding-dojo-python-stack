class User:
    def __init__(self, name):
        self.name = name
        self.user_balance = 0
    
    def make_deposit(self, amount):
        self.user_balance += amount
    
    def make_withdrawal(self, amount):
        self.user_balance -= amount
    
    def display_user_balance(self):
        print(f'User: {self.name}, Balance: ${self.user_balance}')
    
    def transfer_money(self, other_user, amount):
        self.user_balance -= amount
        other_user.user_balance += amount

guido = User("Guido van Rossum")
bill = User("Bill Gates")
zuck = User("Mark Zuckerberg")

guido.make_deposit(10000)
guido.make_deposit(20000)
guido.make_deposit(30000)
guido.make_withdrawal(150)
guido.display_user_balance()

bill.make_deposit(10000)
bill.make_deposit(30000)
bill.make_withdrawal(4000)
bill.make_withdrawal(3500)
bill.display_user_balance()

zuck.make_deposit(100000)
zuck.make_withdrawal(30000)
zuck.make_withdrawal(25000)
zuck.make_withdrawal(14550)
zuck.display_user_balance()

guido.transfer_money(zuck, 10000)
guido.display_user_balance()
zuck.display_user_balance()