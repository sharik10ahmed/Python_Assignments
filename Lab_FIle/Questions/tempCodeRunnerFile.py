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