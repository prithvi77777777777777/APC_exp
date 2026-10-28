class Printer:
    def print_document(self, text): print("Printing:", text)

class Scanner:
    def scan_document(self): print("Scanning document...")

class MultifunctionDevice(Printer, Scanner):
    pass

device = MultifunctionDevice()
device.print_document("Assignment.pdf")
device.scan_document()
