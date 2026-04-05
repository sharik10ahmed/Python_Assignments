# Define three numbers
num1 = 10
num2 = 25
num3 = 15

# Compare the numbers
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}")