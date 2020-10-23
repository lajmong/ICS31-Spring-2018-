# ICS 31 Lab sec 5. Lab Assignment 1d.
def factorial (n: int) -> int:
    ''' Compute n! (n factorial) '''
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)
assert factorial(0) == 1
assert factorial(5) == 120

print("10! is", factorial(10))
print("100! is", factorial(100))
print("120! is", factorial(120))
print("(50 * 10)! is", factorial(50 * 10))
print("factorial(5)! is", factorial(factorial(5)))
