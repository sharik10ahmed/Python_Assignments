# def fact(n):
#     if n==0 or n==1:
#        return 1
#     return n*fact(n-1)


def fact(n):
    if n == 0 or n == 1:  # Added colon
        return 1
    return n * fact(n - 1) # Indented to stay inside the function

print(fact(5))