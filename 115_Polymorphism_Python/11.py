class Product:
    def __init__(self, name, price): self.name, self.price = name, price
    def __eq__(self, other): return self.price == other.price
    def __gt__(self, other): return self.price > other.price
p1, p2 = Product("Mouse", 700), Product("Keyboard", 1200)
print("Same price?", p1 == p2)
print("Mouse costs more?", p1 > p2)
