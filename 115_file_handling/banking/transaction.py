def deposit(account, amount):
    if amount <= 0: raise ValueError('amount must be positive')
    updated = account.copy(); updated['balance'] += amount; return updated
def withdraw(account, amount):
    if amount <= 0 or amount > account['balance']: raise ValueError('invalid amount or insufficient balance')
    updated = account.copy(); updated['balance'] -= amount; return updated
