#write a program to convert to decimal to binary, octal,hexadecimal

choice=int(input("Enter choice 1 to convert decimal to binary 2 to convert decimal to octal 3 to convert decimal to hexadecimal:"))
if choice == 1:
    num=int(input("Enter number to convert decimal to binary: "))
    deci=0
    while num>0:
        rem=num%2
        print(rem)
        deci=deci*10+rem
        num/=2
    print("binary of given is :",deci)