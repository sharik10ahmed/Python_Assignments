# Step 1: Get the initial string from the user
text = input("Enter a string: ")

# Step 2: Use a 'while True' loop to keep showing the menu until the user wants to quit
while True:
    print("\n--- Menu ---")
    print("1. Find frequency of a character")
    print("2. Replace a character")
    print("3. Remove the first occurrence of a character")
    print("4. Remove all occurrences of a character")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    # Operation A: Find frequency
    if choice == '1':
        char = input("Enter character to count: ")
        print("Frequency:", text.count(char))
        
    # Operation B: Replace a character
    elif choice == '2':
        old_char = input("Enter character to replace: ")
        new_char = input("Enter the new character: ")
        text = text.replace(old_char, new_char)
        print("Result:", text)
        
    # Operation C: Remove FIRST occurrence only
    elif choice == '3':
        char = input("Enter character to remove (first only): ")
        # The '1' means it will only replace the first one it finds with nothing ("")
        text = text.replace(char, "", 1) 
        print("Result:", text)
        
    # Operation D: Remove ALL occurrences
    elif choice == '4':
        char = input("Enter character to remove (all): ")
        # Replacing with an empty string ("") effectively deletes it
        text = text.replace(char, "") 
        print("Result:", text)
        
    # Exit the program
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break # This breaks out of the 'while True' loop
        
    # Handling invalid inputs
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")