# a) Define the function that accepts three arguments
def display_collections(my_list, my_tuple, my_dict):
    print("Inside the Function")
    
    # b) Display elements
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Dictionary:", my_dict)

# Prepare the data
fruits_list = ["Apple", "Banana"]
colors_tuple = ("Red", "Yellow")
price_dict = {"Apple": 1.5, "Banana": 0.5}

# Call the function
display_collections(fruits_list, colors_tuple, price_dict)