'''Write a PYTHON program  find a factorial of given number
'''

n=int(input("Enter number to find factorial:"))
fact=1
while(n>0):
    fact=fact*n
    n-=1
print(fact)