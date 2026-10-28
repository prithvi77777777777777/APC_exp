class Vehicle:
    def __init__(self, brand, model):
        self.brand, self.model = brand, model

    def display(self):
        print(f"Brand: {self.brand}\nModel: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type, self.price = fuel_type, price

    def display(self):
        super().display()
        print(f"Fuel: {self.fuel_type}\nPrice: ₹{self.price:.2f}")

    def discounted_price(self, discount_percent):
        return self.price * (1 - discount_percent / 100)

car = Car("Tata", "Nexon", "Petrol", 900000)
car.display()
print("Price after 10% discount: ₹", car.discounted_price(10))
