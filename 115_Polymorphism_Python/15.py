class SmartDevice:
    def turn_on(self): print("Device on")
    def turn_off(self): print("Device off")
class Light(SmartDevice):
    def turn_on(self): print("Light switched on")
    def turn_off(self): print("Light switched off")
class Fan(SmartDevice):
    def turn_on(self): print("Fan started")
    def turn_off(self): print("Fan stopped")
class AC(SmartDevice):
    def turn_on(self): print("AC cooling started")
    def turn_off(self): print("AC stopped")
class TV(SmartDevice):
    def turn_on(self): print("TV switched on")
    def turn_off(self): print("TV switched off")
for d in [Light(), Fan(), AC(), TV()]:
    d.turn_on(); d.turn_off()
