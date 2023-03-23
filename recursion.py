# factorial = factorial * (n - 1)

def factorial(n):
    if ( n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)   # calling the functions in his own function

print(factorial(5))


