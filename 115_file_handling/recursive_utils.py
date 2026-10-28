def factorial(n):
    if n < 0: raise ValueError("n must be non-negative")
    return 1 if n <= 1 else n * factorial(n - 1)
def fibonacci(n):
    if n < 0: raise ValueError("n must be non-negative")
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
def sum_digits(n):
    return n if n < 10 else n % 10 + sum_digits(n // 10)
def to_binary(n):
    if n < 0: raise ValueError("n must be non-negative")
    return "0" if n == 0 else bin(n)[2:]
