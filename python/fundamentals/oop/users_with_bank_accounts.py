class BankAccount:
    all_accounts = []
    
    def __init__(self, balance, int_rate):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        return f'Balance: ${self.balance}'
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
    
    @classmethod
    def all_balances(cls):
        [print(f'Balance: ${account.balance}') for account in cls.all_accounts]


class User:
    def __init__(self, name):
        self.name = name
        self.account = {}
    
    def create_account(self, account_name, balance = 0, int_rate = 0):
        new_account = {account_name: BankAccount(balance, int_rate)}
        self.account.update(new_account)
        return self
    
    def make_deposit(self, account_name, amount):
        self.account[account_name].deposit(amount)
        return self
    
    def make_withdrawal(self, account_name, amount):
        self.account[account_name].withdraw(amount)
        return self
    
    def display_user_balance(self, account_name):
        print(f'User: {self.name}, {account_name.title()} {self.account[account_name].display_account_info()}')
        return self
    
    def transfer_money(self, own_account_name, other_user, other_account_name, amount):
        self.make_withdrawal(own_account_name, amount)
        other_user.make_deposit(other_account_name, amount)
        print()
        self.display_user_balance(own_account_name)
        other_user.display_user_balance(other_account_name)

guido = User("Guido van Rossum")
guido.create_account("savings", 1000, .02).create_account("time deposit", 2000, .04).make_deposit("savings", 100).make_deposit("time deposit", 2000).make_withdrawal("savings", 50).display_user_balance("savings").display_user_balance("time deposit")

zuck = User("Mark Zuckerberg")
zuck.create_account("checking", 10000).transfer_money("checking", guido, "savings", 2000)