#write a program to check number is palindrome is not

num=int(input("Enter a number to check palindrome or not: "))
rev=0
temp=num
for i in range(1,len(str(num))+1):
    rem=num%10
    num//=10
    rev=(rev*10)+rem
    print(rev)
if temp == rev:
    print(temp," is palindrome number ")
else:
    print(temp," is not palindrome number ")