from mathutils.basic import add, multiply
from mathutils.number import is_prime, is_palindrome, is_armstrong
from mathutils.statistics import mean, maximum, minimum

print("2 + 3 =", add(2, 3))
print("2 * 3 =", multiply(2, 3))
print("Is 7 prime?", is_prime(7))
print("Is 121 palindrome?", is_palindrome(121))
print("Is 153 Armstrong?", is_armstrong(153))
values = [10, 20, 30, 40]
print("Mean:", mean(values))
print("Maximum:", maximum(values))
print("Minimum:", minimum(values))
