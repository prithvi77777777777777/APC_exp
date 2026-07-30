#Write a PYTHON program to produce following design
     #  A B
   #   A B C
  #    A B C D 
 #     A B C D E
#      If user enters n value as 5


n=int(input("Enter value for n:"))
asci=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end=" ")

    print()
