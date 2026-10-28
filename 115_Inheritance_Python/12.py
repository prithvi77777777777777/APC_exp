class Product:
    def __init__(self, product_id, name, price):
        self.product_id, self.name, self.price = product_id, name, price

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty_years):
        super().__init__(product_id, name, price)
        self.brand, self.warranty_years = brand, warranty_years

    def final_price(self, discount_percent):
        return self.price * (1 - discount_percent / 100)

p = ElectronicProduct(1, "Laptop", 60000, "Lenovo", 2)
print(vars(p), "| Price after discount: ₹", p.final_price(12))
