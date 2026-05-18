def iseven(number):
    if number % 2 == 0:
       return True
    else:
       return False
num = int(input("Enter a number-> "))

print(f"Is {num} is even? -> {iseven(num)}")
