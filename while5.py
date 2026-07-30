'''Write a PYTHON program to print sum of odd numbers up to n
'''

n=int(input("Enter number:"))
sum=0
c=1
while(c<=n):
    
    sum+=c
    c+=2
print(sum)