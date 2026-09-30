# Q3. A company insures its drivers in the following cases:
# - If the driver is married.
# - If the driver is unmarried, male and above 30 years of age.
# - If the driver is unmarried, female and above 25 years of age.
# In all other cases, the driver is not insured.
# Write a PYTHON program to determine whether the driver is insured or not.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

marital_status = input("Enter marital status (married/unmarried): ").lower()
gender = input("Enter gender (male/female): ").lower()
age = int(input("Enter age: "))

if marital_status == "married":
    print("The driver is INSURED")
elif marital_status == "unmarried" and gender == "male" and age > 30:
    print("The driver is INSURED")
elif marital_status == "unmarried" and gender == "female" and age > 25:
    print("The driver is INSURED")
else:
    print("The driver is NOT INSURED")