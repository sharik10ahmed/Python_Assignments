def isprime(number):
    if number <=1:
       return False
    
    for i in range(2,number):
        if number % i == 0:
           return False
    return True

test_num = int(input("Enter a number-> "))

if isprime(test_num):
   print(f"{test_num} is a prime")
else:
   print(f"{test_num} is not a prime")

