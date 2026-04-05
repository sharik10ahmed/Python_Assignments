# Ask the user to input the student's marks
# Using float() allows for decimal marks (like 85.5)
marks = float(input("Enter the student's marks (0-100): "))

# Check for invalid input first (optional, but good practice)
if marks > 100 or marks < 0:
    print("Invalid marks! Please enter a number between 0 and 100.")
# Check for Grade A
elif marks >= 90:
    print("Grade A")
# Check for Grade B
elif marks >= 75:
    print("Grade B")
# Check for Grade C
elif marks >= 50:
    print("Grade C")
# If it's none of the above, it must be below 50
else:
    print("Grade F")