class Payment:
    def make_payment(self, amount): raise NotImplementedError
class UPIPayment(Payment):
    def make_payment(self, amount): print(f"Paid ₹{amount} using UPI")
class CardPayment(Payment):
    def make_payment(self, amount): print(f"Paid ₹{amount} using card")
class WalletPayment(Payment):
    def make_payment(self, amount): print(f"Paid ₹{amount} using wallet")
def checkout(method, amount): method.make_payment(amount)
for method in [UPIPayment(), CardPayment(), WalletPayment()]: checkout(method, 499)
