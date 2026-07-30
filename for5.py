#Write a PYTHON program to sum the given sequence
#      1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!
n=int(input("Enter the value of n: ")) 
ans=0
fact=1
for i in range(n+1):
    for j in range(1,i+1):
        fact=fact*j
    ans=ans+(1/fact)
    fact=1

print("The sum of the given sequence is: ",ans)