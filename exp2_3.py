#write a program to calculate factorial of number to check the number is prime or not

choice=int(input("Enter choice 1 to find factorial 2 to check the number is prime or not:"))
if choice == 1:
    num=int(input("Enter number to find factorial: "))
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(f"factorial of {num} is :",fact)
else:
    num=int(input("Enter to find number is prime or not : "))
    isprime=True
    for i in range(2,(num//2)+1):
        if num % i == 0:
            isprime=False

    if isprime == False:
        print(f"{num} is not prime number")
    else:
        print(f"{num} is prime number")
    