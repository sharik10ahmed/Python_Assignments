# --- 12. isdigit() Examples ---

str1 = "12345"
str2 = "123a45"
str3 = "12.34" 
str4 = " " # Space character

print("--- isdigit() ---")
print(f"'{str1}' isdigit():", str1.isdigit())  # True: All characters are digits
print(f"'{str2}' isdigit():", str2.isdigit())  # False: Contains a letter ('a')
print(f"'{str3}' isdigit():", str3.isdigit())  # False: Contains a decimal point ('.')
print(f"'{str4}' isdigit():", str4.isdigit())  # False: Space is not a digit


# --- 11. isalpha() Examples ---

str5 = "Python"
str6 = "Python3"
str7 = "Hello World"

print("\n--- isalpha() ---")
print(f"'{str5}' isalpha():", str5.isalpha())  # True: All characters are alphabetic letters
print(f"'{str6}' isalpha():", str6.isalpha())  # False: Contains a digit ('3')
print(f"'{str7}' isalpha():", str7.isalpha())  # False: Contains a space