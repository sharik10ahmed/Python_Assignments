def count_frequency(text):
    # Create an empty dictionary
    freq_dict = {}
    
    # Check every character in the text
    for char in text:
        if char in freq_dict:
            freq_dict[char] = freq_dict[char] + 1  # Add 1 if it exists
        else:
            freq_dict[char] = 1                    # Start at 1 if it's new
            
    return freq_dict