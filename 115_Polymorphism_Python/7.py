class BankAccount:
    def __init__(self, balance): self.balance = balance
    def calculate_interest(self): return 0
class SavingsAccount(BankAccount):
    def calculate_interest(self): return self.balance * 0.04
class CurrentAccount(BankAccount):
    def calculate_interest(self): return 0
class FixedDepositAccount(BankAccount):
    def calculate_interest(self): return self.balance * 0.07
for a in [SavingsAccount(10000), CurrentAccount(10000), FixedDepositAccount(10000)]:
    print(type(a).__name__, "interest:", a.calculate_interest())
