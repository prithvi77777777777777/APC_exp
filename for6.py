#Write a PYTHON program to compute the cosine series
#          cos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!

x=int(input("Enter value for x:"))
n=int(input("Enter value for n:"))
sign=0
cosx=1
for i in range(2,n+1,2):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    temp=x
    for t in range(1,i):
        temp=temp*x
    if sign%2 ==0:
        
        cosx=cosx-(temp/fact)
    
    else:
        cosx=cosx+(temp/fact)
    sign+=1

print("Cos(x)=",cosx)