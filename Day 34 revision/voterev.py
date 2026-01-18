age = int(input("Enter your age= "))

if age < 18:
    print("You are not eligible to vote")
else:
    citizenship = input("Enter your citizenship-> ")
    if citizenship.lower() == "indian":
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")