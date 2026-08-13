num={1,2,4,6,7,3,5,8,9,10}
n=int(input("Enter a number to delete: "))
if n not in num:
    print("Number not found in the set")
else:
    num.remove(n)
    print("After deleting",n,"the set is:",num)