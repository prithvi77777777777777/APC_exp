'''Write a PYTHON program to print sum of even numbers up to n
'''


n=int(input("Enter number:"))
c=2
sum=0.0
while(c<=n):
    sum+=c
    c+=2

print(sum,end=" ")