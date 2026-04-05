# Step 1: Read 'n' from the user
n = int(input("Enter the number of terms (n): "))

# Step 2: Create a variable to keep track of the running total
total_sum = 0

# Step 3: Loop through all numbers from 1 up to 'n'
# We use (n + 1) because the range() function stops exactly one number before the end.
for i in range(1, n + 1):
    
    # Step 4: Check if the number is even
    if i % 2 == 0:
        total_sum = total_sum - i  # Subtract even numbers
    
    # Step 5: Otherwise, the number must be odd
    else:
        total_sum = total_sum + i  # Add odd numbers

# Step 6: Print the final result
print("The sum of the series up to", n, "terms is:", total_sum)