def letter_frequency(sentence):
    # Initialize empty dictionary to store letter frequencies
    freq_dict = {}
    
    # Convert sentence to lowercase and iterate through each character
    for char in sentence.lower():
        # Check if character is a letter
        if char.isalpha():
            # Increment count in dictionary (default 0 if new letter)
            freq_dict[char] = freq_dict.get(char, 0) + 1
    
    return freq_dict

# Get input from user
user_sentence = input("Enter a sentence: ")

# Calculate and display frequencies
frequencies = letter_frequency(user_sentence)

# Display results
print("\nLetter frequencies:")
for letter, count in sorted(frequencies.items()):
    print(f"{letter}: {count}")
