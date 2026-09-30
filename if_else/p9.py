# Q2. Write a PYTHON program to check a year for leap year.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a LEAP YEAR")
else:
    print(year, "is NOT a leap year")