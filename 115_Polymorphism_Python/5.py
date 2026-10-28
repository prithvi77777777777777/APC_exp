class Notification:
    def send(self, message): raise NotImplementedError
class EmailNotification(Notification):
    def send(self, message): print("Email:", message)
class SMSNotification(Notification):
    def send(self, message): print("SMS:", message)
class PushNotification(Notification):
    def send(self, message): print("Push notification:", message)
for n in [EmailNotification(), SMSNotification(), PushNotification()]:
    n.send("Your order has shipped.")
