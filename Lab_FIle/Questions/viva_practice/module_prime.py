from sympy import isprime

test_num = int(input("Enter a number-> "))
if isprime(test_num):
   print(f"{test_num} is a prime")
else:
   print(f"{test_num} is not a prime")