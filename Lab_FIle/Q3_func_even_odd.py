# Step 1: Define the function with 'number' as its parameter
def is_even(number):
    
    # Step 2: Check if the remainder is 0 when divided by 2
    if number % 2 == 0:
        return True   # It is Even
    else:
        return False  # It is Odd

# --- Testing the code ---
test_number_1 = int(input("Enter first no.-> "))
test_number_2 = int(input("Enter second no.-> "))

# Calling the function and printing the results
print(f"Is {test_number_1} even?", is_even(test_number_1))
print(f"Is {test_number_2} even?", is_even(test_number_2))