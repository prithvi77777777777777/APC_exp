class Camera:
    def take_photo(self): print("Photo captured.")

class Phone:
    def make_call(self, number): print("Calling", number)

class Smartphone(Camera, Phone):
    pass

phone = Smartphone()
phone.take_photo()
phone.make_call("9876543210")
