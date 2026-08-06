'''6.	Write a program to find the largest and smallest number in a list without using max() or min().'''
li=[12,1335,56,8,934,123]
min=li[0]
max=-1
print("list is :",li)
for i in li:
    if max  < i:
        max=i
    if min > i:
        min=i

print("Max element is :",max,"min element is :",min)