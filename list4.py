'''4.	Create a list of numbers. Add:
•	One element at the end 
•	One element at the beginning 
•	One element at a specified position 
Display the updated list.
'''

li=[12,123,4623,25]
print(li)
li.insert(0,10)
print("After insertion at first:")
print(li)
print("After adding element at the end:")
li.append(1021)
print(li)
n=int(input("Enter position to add element:"))
n1=int(input("Enter  element to add :"))
li.insert(n,n1)
print("After adding element at specified position:")
print(li)