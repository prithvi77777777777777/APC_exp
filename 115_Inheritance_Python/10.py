class Vehicle:
    def __init__(self, brand): self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand); self.doors = doors

class Bike(Vehicle):
    def __init__(self, brand, engine_cc):
        super().__init__(brand); self.engine_cc = engine_cc

class SportsCar(Car):
    def __init__(self, brand, doors, top_speed):
        super().__init__(brand, doors); self.top_speed = top_speed

class ElectricBike(Bike):
    def __init__(self, brand, engine_cc, range_km):
        super().__init__(brand, engine_cc); self.range_km = range_km

print(vars(SportsCar("Porsche", 2, 300)))
print(vars(ElectricBike("Ather", 0, 120)))
