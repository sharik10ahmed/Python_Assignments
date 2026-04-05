# Step 1: Read m and n from the user
# input() gets text from the user, int() turns that text into a whole number
m = int(input("Enter the base number (m): "))
n = int(input("Enter the power (n): "))

# Step 2: Calculate using the '**' operator
result = m ** n

# Step 3: Print the result
print(m, "raised to the power of", n, "is", result)