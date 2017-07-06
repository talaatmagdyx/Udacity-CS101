# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    fac = 1
    i = 1
    while i <= n:
        fac = i * fac
        i = i + 1
    return fac


print (factorial(4))
