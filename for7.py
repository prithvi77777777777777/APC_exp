#Write a short PYTHON program to check weather the 
#     square root of number is prime or  not.
import math
n=float(input("Enter to check its sqrt is prime number or not :"))
sq=round(math.sqrt(n))

isprime=True
for i in range(2,sq):
    if sq% i ==0:
        isprime=False

if isprime!=True:
    print(f"{n} is not prime number")
else:
    print(f"{n} is  prime number")
    