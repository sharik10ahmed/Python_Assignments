## SOme methods in string :
# 1. len() => it is used to find the length of string
# 2. lower() => it is used to convert the string to lowercase
# 3. upper() => it is used to convert the string to uppercase
# 4. title() => it is used to convert the first character of each word to uppercase
# 5. strip() => it is used to remove the leading and trailing whitespace from the string
# 6. replace() => it is used to replace a substring with another substring
# 7. split() => it is used to split the string into a list of substrings based
# 8. join() => it is used to join a list of strings into a single string with a specified separator
# 9. find() => it is used to find the index of the first occurrence of a substring
# 10. count() => it is used to count the number of occurrences of a substring in the string
# 14. startswith() => it is used to check if the string starts with a specified substring
# 15. endswith() => it is used to check if the string ends with a specified substring
# # 16. index() => it is used to find the index of the first occurrence of a substring (raises an error if not found)
# 17. capitalize() => it is used to convert the first character of the string to uppercase and the rest to lowercase
sentence = "This is a sample sentence."
print((len("Hello World")))  # 11
print("Hello World".lower())  # hello world on a specified delimiter
print("Hello World".upper())  # HELLO WORLD on a specified delimiter
print(sentence.title())  # Hello World
print("   Hello World   ".strip())  # Hello World
print("Hello World".replace("World", "Python"))  # Hello Python
print("Hello World".split(" "))  # ['Hello', 'World']
print("-".join(["Hello", "World"]))  # Hello-World
print("Hello World".find("l"))  # 6
print("Hello World".count("o"))  # 2
print("Hello World".startswith("H"))  # True
print("Hello World".endswith("World"))  # True
print("Hello World".index("W"))  # 6
print("hello world".capitalize())  # Hello world on a specified delimiter
# 11. isalpha() => it is used to check if all characters in the string are alphabetic
# 12. isdigit() => it is used to check if all characters in the string