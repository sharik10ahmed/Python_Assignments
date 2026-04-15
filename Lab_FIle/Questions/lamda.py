# The input list
numbers = [2, 4, 6, 8]

# 1. Assert statement (The Security Guard)
# It checks if the list is NOT empty. If it is empty, the program stops with an error.
assert len(numbers) > 0, "Error: The list is empty!"

# 2. Lambda function with map
# lambda x: x**2 is the tiny function that squares each number
# map() applies that lambda to every item in the 'numbers' list
squares = list(map(lambda x: x**2, numbers))

# Display the result
print("Original numbers:", numbers)
print("Squared numbers:", squares)