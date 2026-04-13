def safe_division(num1, num2):
    try:
        result = num1 / num2
        print(f"Result: {result}")
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
        return None

# Test the function
print("Test 1 - Normal division:")
safe_division(10, 2)

print("\nTest 2 - Division by zero:")
safe_division(10, 0)

print("\nTest 3 - User input example:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
safe_division(num1, num2)
