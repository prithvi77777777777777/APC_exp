# Q4. Write a PYTHON program to reverse the given number.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

n = int(input("Enter a number: "))

temp = n
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reverse of", n, "is:", reverse)