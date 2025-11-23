def palindrome_checker():
    word = input("Enter Your Desired Word -> ")
    reverser=""
    for i in word:
        reverser = i + reverser
    if word == reverser:
        print("True")
    else:
        print("False")

palindrome_checker()
