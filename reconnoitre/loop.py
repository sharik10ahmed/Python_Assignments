 # Initialize the variable to enter the loop

# The loop will continue as long as the user_input is NOT "close"
while user_input.lower() != "close":
    # --- Program Code Block ---
    
    # 1. Run your program logic here (e.g., call a function, process data, etc.)
    print("--- Running your main program logic! ---")
    
    # Example: Print the result of your Calc_IF.py file or similar logic
    print("Calculation successful.") 
    
    # --- End Program Code Block ---
    
    # 2. Prompt the user for input to control the loop
    user_input = input("Program finished. Type 'close' to exit, or press Enter to run again: ")
    print("-" * 30) # Separator for clarity

print("Program successfully closed. Goodbye!")