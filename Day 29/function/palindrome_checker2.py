def palindrome(word):
    reverser= ""
    for i in word:
        reverser = i + reverser
    if word == reverser:
        return True
    else:
        return False
user_word=input("Enter your desired word -> ")
result = palindrome(user_word)
if result == True:
    print("It is palindrome")
else:
    print("It is not palindrome")

