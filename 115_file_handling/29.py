import recursive_utils

number = int(input("Enter a non-negative integer: "))
print("Factorial:", recursive_utils.factorial(number))
print("Fibonacci series:", recursive_utils.fibonacci(number))
print("Sum of digits:", recursive_utils.sum_digits(number))
print("Binary:", recursive_utils.to_binary(number))
