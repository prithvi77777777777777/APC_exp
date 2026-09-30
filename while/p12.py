# Q3. Write a PYTHON program to check the entered number is palindrome or not
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

n = int(input("Enter a number: "))

temp = n
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if reverse == n:
    print(n, "is a PALINDROME number")
else:
    print(n, "is NOT a palindrome number")