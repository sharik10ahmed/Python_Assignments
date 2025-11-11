my_text = "Sharik"
vowels = "aeiou"
print("vowels","consonants".center(20))
for check in my_text:
    if check in vowels:
        print(check)
    if check not in vowels:
        print(f"\t\t{check}")