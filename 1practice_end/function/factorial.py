def factorial(p):
    factorial=1
    for i in range(1,p+1):
        factorial = factorial*i
    print(factorial)
factorial(5)

def factorial(p):
    result = 1  # We start with 1 because multiplying by 0 results in 0
    for i in range(1, p + 1): # Start at 1, stop at p
        result = result * i
    print(result)

factorial(5)