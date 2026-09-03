'''17.	Create a file containing student records in the format:
RollNo,Name,Marks
101,Amit,85
102,Priya,92
103,Rahul,78
'''
with open('studentrecords.txt', 'w') as file:
    file.write("Roll no\t")
    file.write("Name\t")
    file.write("Marks\t")
    n=int(input("Enter the number of records you want to write in file:"))
    for i in range(n):
        r=input("Enter roll no:")
        n=input("Enter name :")
        m=input("Enter marks:")
        file.write("\n")
        file.write(r)
        file.write("\t")
        file.write(n)
        file.write("\t")
        file.write(m)
       
with open('studentrecords.txt', 'r') as file:
    
    for i in file.readline():
        print(i)
    max_marks=0
    avg=0
    count=0
    above80=[]
    for i in file.readline():
        count+=1
        a= i.split("\t")
        avg+=int(a[2])
        if int(a[2])>80:
            above80.append(a[1])
            above80.append(":")
            above80.append(a[2])
            above80.append("\n")

        if int(a[2])>max_marks:
            max_marks=a[2]

            name=a[1]
    avg=avg/count
    print("Average marks of students is:",avg)
    print(above80)