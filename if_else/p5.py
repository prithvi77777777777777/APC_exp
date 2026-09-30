# Q1. Write a PYTHON program to evaluate the student performance.
# If % is >=90 then Excellent performance
# If % is >=80 then Very Good performance
# If % is >=70 then Good performance
# If % is >=60 then Average performance
# else Poor performance.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

percentage = float(input("Enter the percentage: "))

if percentage >= 90:
    print("Excellent Performance")
elif percentage >= 80:
    print("Very Good Performance")
elif percentage >= 70:
    print("Good Performance")
elif percentage >= 60:
    print("Average Performance")
else:
    print("Poor Performance")