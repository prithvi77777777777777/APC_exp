#Write a PYTHON program to check a year for leap year.

n1=int(input("Enter year to check it is leap year or not:"))
if n1 % 4 == 0:
    print(f"{n1} is leap year")
else:
    print(f"{n1} is not a leap year")
