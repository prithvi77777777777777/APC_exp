#Write a PYTHON program that prints  1 2 4 8 16 32 … n2

n=int(input("Enter the value of n: "))
for i in range(n):
    print(2**i)