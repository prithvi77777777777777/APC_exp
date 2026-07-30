'''Write a PYTHON program to print Fibonacci series up to n
'''

a=0
b=1
n=int(input("Enter limit"))

while(b<n):
    ans=a+b
    print( ans,end=" ")
    a=b
    b=ans
print()
print("AABHARII AHOT!!!!!!!    :-) ")
