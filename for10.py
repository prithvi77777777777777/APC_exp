'''Write a PYTHON program to produce following design
       A B C D E
       A B C D
       A B C
       A B
       A                      
      (If user enters n value as 5)'''




n=int(input("Enter value for n:"))
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65+j),end=" ")

    print()