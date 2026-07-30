'''A company insures its drivers in the following cases:- If the driver is married.- If the driver is unmarried, male and above 30 years        
         of age.      - If the driver is unmarried, female and above 25 years of age.
         
        In all the other cases, the driver is not insured.        Write a PYTHON program to determine whether the driver     
        is insured or not
'''

m=input(" Enter m for married and u for unmarried: ")
if m =='m':
    print("Driver is insured")
else:
    g=input("Enter m for male and f for female: ")
    age=int(input("Enter age :"))
    if m == 'u' and g =='m' and age>=30:
        print("Driver is insured")
    elif m == 'u' and g =='f' and age>=25:
        print("Driver is insured")
    else:
        print("Driver is not insured")