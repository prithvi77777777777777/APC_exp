# Q24. Rotate a list left by one position and right by one position.
# Name: Prithviraj Sutar | TY-CSE | Roll No: 115

numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)

left_rotate = numbers[1:] + numbers[:1]
print("Left rotated:", left_rotate)

right_rotate = numbers[-1:] + numbers[:-1]
print("Right rotated:", right_rotate)