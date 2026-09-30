# Q1. Write a PYTHON program to check the entered number is prime or not
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

n = int(input("Enter a number: "))

if n <= 1:
    print(n, "is NOT a prime number")
else:
    i = 2
    is_prime = True
    while i <= n // 2:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(n, "is a PRIME number")
    else:
        print(n, "is NOT a prime number")