lst = [2, 4, 6, 8]

# Ensure the list is not empty
assert len(lst) > 0 

# Apply the square function to every item
square = list(map(lambda x: x*x, lst))

print("square", square)