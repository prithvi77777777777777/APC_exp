class Animal:
    def sound(self): print("Unknown sound")
class Dog(Animal):
    def sound(self): print("Woof")
class Cat(Animal):
    def sound(self): print("Meow")
class Cow(Animal):
    def sound(self): print("Moo")
class Lion(Animal):
    def sound(self): print("Roar")
for a in [Dog(), Cat(), Cow(), Lion()]: a.sound()
