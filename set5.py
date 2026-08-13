students={"rohan","yash","param","harsh"}
name=input("Enter student  name to check: ").lower()
if name in students:
    print(name,"is present in the set")
else:
    print(name,"is not present in the set") 