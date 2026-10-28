class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no, self.balance = account_no, balance

    def display(self):
        print(f"Account: {self.account_no}\nBalance: ₹{self.balance:.2f}")

class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100

class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        super().display()
        print("Interest:", self.calculate_interest(), "| Benefits:", self.benefits)

PremiumSavingsAccount("AC1001", 50000, 5, "Airport lounge access").display()
