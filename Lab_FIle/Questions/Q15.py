import sys # lodasd the tool needed to read terminal commands

# c) Function with default parameters to calculate simple interest
# If rate and time are not provided, it defaults to 5.0% and 2 years.
def calculate_si(principal, rate=5.0, time=2.0): # just for the function (For SI)
    return (principal * rate * time) / 100

# --- a & b) Check for Command Line Arguments for quick Arithmetic ---
if len(sys.argv) == 3: #it needs 3 items (basically it checks for 3 items) # Checks if you typed two numbers next to the script name (when user enter in terminal)
    print("--- Command Line Math Detected ---")
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    print(f"Addition of {num1} and {num2} = {num1 + num2}")
    print("----------------------------------\n")

# --- Interactive Menu System ---
while True:  # infinite loop to display the main menu 
    print("\n=== MAIN MENU ===")
    print("1. Perform Arithmetic (Add & Multiply)")
    print("2. Calculate S.I (Use Default 5% Rate & 2 Years)")
    print("3. Calculate S.I (Provide Custom Rate & Time)")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':   # Asks for the numbers to perform operations
        a = float(input("Enter first num: "))
        b = float(input("Enter second num: "))
        print(f"-> Addition: {a + b}")
        print(f"-> Multiplication: {a * b}")
        
    elif choice == '2':  # Just asks for the principal and use default parameters
        p = float(input("Enter Principal amt: "))
        # We only pass the principal; the function uses its default rate and time
        interest = calculate_si(p)
        print(f"-> S.I (at default 5% for 2 yrs): {interest}")
        
    elif choice == '3': # Asks for principal, rate, and time.
        p = float(input("Enter Principal amt: "))
        r = float(input("Enter Rate of Interest: "))
        t = float(input("Enter Time in years: "))
        # We pass all three, overwriting the defaults
        interest = calculate_si(p, r, t)
        print(f"-> S.I (at {r}% for {t} yrs): {interest}")
        
    elif choice == '4': # it kills the loop
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please select a num from 1 to 4.")