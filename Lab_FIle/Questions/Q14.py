# Import the toolbox we just made
import my_module

# The string we want to test
my_string = "hello"

# Use the function from our module
# We use 'my_module.' to tell Python exactly where to look
result = my_module.count_frequency(my_string)

print("Original string:", my_string)
print("Character frequency:", result)