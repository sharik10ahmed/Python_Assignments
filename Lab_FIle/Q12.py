# Step 1: Get numbers from the user and split them by spaces
user_input = input("Enter numbers separated by spaces: ")
string_list = user_input.split()

# Step 2: Convert the text input into a list of actual integers
numbers = []
for item in string_list:
    numbers.append(int(item))

# Step 3: Check if the length of the list matches the length of a set
if len(numbers) != len(set(numbers)):
    # Step 4: Throw an exception if they don't match
    raise Exception("Error: Duplicate numbers were found in your list!")

# Step 5: If we make it here, the numbers are safe
print("Success! Your unique list is:", numbers)