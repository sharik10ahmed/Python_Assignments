def find_all_indices(main_str, substr):
    indices = []
    start = 0
    
    while True:
        pos = main_str.find(substr, start)
        if pos == -1:  # Substring not found
            break
        indices.append(pos)
        start = pos + 1  # Continue searching after current match
    
    return indices if indices else -1

# Main program
str1 = input("Enter main string: ")
str2 = input("Enter substring to find: ")

result = find_all_indices(str1, str2)

if result == -1:
    print("-1")
else:
    print(f"Indices: {result}")
