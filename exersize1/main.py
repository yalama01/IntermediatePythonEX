# import the BankAccount class, instantiate it with a hardcoded account_name and starting_balance, deposit any amount, withdraw any amount, and then print out the result of calling the get_balance method on that class instance.

from BankAccount import BankAccount

account = BankAccount("John", 1000)
account.deposit(100)
account.withdraw(200)
print(account.getBalance())