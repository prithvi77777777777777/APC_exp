#write a program to convert pound into kg, kilometer into miles

choice=int(input("Enter 1 to convert pound into kg or 2 to convert kilometer into miles: "))
if choice == 1:
    pou=float(input("Enter weight in pounds"))
    print("Equivalent weight in kilo will be:",pou*0.453592)
else:
    km=float(input("Enter distance in kilometers: "))
    print("Equivalent distance in miles will be:",km*0.621371)