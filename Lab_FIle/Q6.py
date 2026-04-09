def find_all_occurrences(main_string, sub_string):
    # Step 1: Create an empty list to store our winning indices
    indices = []
    
    # Step 2: Get the lengths of both strings
    main_len = len(main_string)
    sub_len = len(sub_string)
    
    # Step 3: Slide the window across the main string
    # We stop early so our window doesn't go off the edge of the word
    for i in range(main_len - sub_len + 1):
        
        # Slice out a chunk of the main string that is the same size as the sub_string
        chunk = main_string[i : i + sub_len]
        
        # Step 4: Compare the chunk to our sub_string
        if chunk == sub_string:
            indices.append(i) # We found a match! Save the index 'i'
            
    # Step 5: Check if we found any matches at all
    if len(indices) == 0:
        return -1
    else:
        return indices

# --- Testing the code ---
text = "banana"
search_word = "na"
missing_word = "cat"

print("Finding 'na' in 'banana':", find_all_occurrences(text, search_word))
print("Finding 'cat' in 'banana':", find_all_occurrences(text, missing_word))