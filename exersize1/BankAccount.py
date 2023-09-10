
class BankAccount:
    accountName = ""
    balance = 0.0
    
    def __init__(self, accountName, balance):
        self.accountName = accountName
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
    
    def getBalance(self):
        return '{account_name} has a balance of {balance}'.format(account_name=self.accountName, balance=self.balance)