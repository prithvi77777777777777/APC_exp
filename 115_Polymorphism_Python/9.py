class Distance:
    def __init__(self, feet, inches):
        total = feet * 12 + inches
        self.feet, self.inches = divmod(total, 12)
    def __add__(self, other):
        return Distance(0, self.feet * 12 + self.inches + other.feet * 12 + other.inches)
    def __str__(self): return f"{self.feet} feet {self.inches} inches"
print(Distance(5, 10) + Distance(3, 8))
