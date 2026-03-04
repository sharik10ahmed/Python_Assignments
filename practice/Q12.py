text = input("Enter string: ").lower()
v = 0
c = 0

for char in text:
    if char.isalpha():
        if char in "aeiou":
            v += 1
        else:
            c += 1

print("Vowels-> ",v, "Consonants-> ",c)