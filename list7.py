'''7.	Accept 10 numbers from the user and store them in a list. Calculate:
•	Sum 
•	Average 
'''
sum=0
li=[]
for i in range(10):
    p=int(input(f"Enter {i} element:"))
    li.append(p)
    sum+=p
avg=sum/10
print(li)
print(sum)
print(avg)