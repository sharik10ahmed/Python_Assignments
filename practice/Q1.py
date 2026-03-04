# 1. Coding: Defining the problem and logic
def check_status(battery_level):
    
    # 2. Running: The interpreter executes this line by line
    if battery_level > 20:
        print("Battery is good.")
    else:
        # 3. Debugging: If the output is wrong, we can easily change the logic here
        print("Low battery! Please charge.")

# Testing the code
check_status(15)