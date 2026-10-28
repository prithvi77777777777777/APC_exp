class Vehicle:
    def start(self): print("Vehicle starting")
class Car(Vehicle):
    def start(self): print("Car starts with a key/button")
class Bike(Vehicle):
    def start(self): print("Bike starts with a self-start/kick")
class Bus(Vehicle):
    def start(self): print("Bus engine starts")
for v in [Car(), Bike(), Bus()]: v.start()
