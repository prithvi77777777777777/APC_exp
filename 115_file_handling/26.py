from number_utils import is_prime, is_palindrome, is_armstrong, is_perfect

number = int(input("Enter a non-negative integer: "))
print("Prime:", is_prime(number))
print("Palindrome:", is_palindrome(number))
print("Armstrong:", is_armstrong(number))
print("Perfect:", is_perfect(number))
