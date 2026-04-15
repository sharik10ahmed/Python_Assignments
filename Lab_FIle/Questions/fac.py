# a) Define the function
def calculate_factorial(n):
    result = 1
    # Loop from 1 up to n
    for i in range(1, n + 1):
        result = result * i
    return result

# b) Call the function and display result
number = 5
answer = calculate_factorial(number)

print(f"The factorial of {number} is: {answer}")