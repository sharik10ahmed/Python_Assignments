name = input("Name: ")
char = input("Character: ")

length = len(name.replace(" ", ""))
count = name.lower().count(char.lower())

print("Length:", length)
print("Count:", count)