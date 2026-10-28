from banking.account import create_account
from banking.transaction import deposit, withdraw
from banking.loan import calculate_simple_interest

account = create_account("Asha", 1000)
account = deposit(account, 500)
account = withdraw(account, 200)
print(account)
print("Simple loan interest:", calculate_simple_interest(10000, 8, 2))
