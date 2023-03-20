class BankAccount:
    all_accounts = []
    
    def __init__(self, balance = 0, int_rate = 0.01):
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
        print(f'Balance: ${self.balance}')
        return self
    
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

account_1 = BankAccount()
account_2 = BankAccount()

account_1.deposit(100).deposit(200).deposit(300).withdraw(50).yield_interest().display_account_info()
account_2.deposit(1000).deposit(2000).withdraw(1000).withdraw(1500).withdraw(250).withdraw(500).yield_interest().display_account_info()

BankAccount.all_balances()