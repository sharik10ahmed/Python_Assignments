A_Word="Program"

A_Word2="Software"

A_sentence="a person is walking."

A_sentence2="      a person is walking."


print(len(A_Word))

print("Lower",A_Word.lower())

print("UPPER",A_Word.upper())

print("TITLE",A_sentence.title())

print("STRIP",A_sentence2.strip())

print("REPLACE",A_sentence.replace("person","pedestrian"))

print("Split",A_sentence.split())

print("Join -> ","_".join(A_Word))

print("Find -> ",A_Word.find("m"))  # 6

print("Count -> ",A_Word.count("o"))  # 2
print("Startswith -> ",A_Word.startswith("P"))  # True
print("Endswith -> ",A_Word.endswith("m"))  # True
print("Index -> ",A_Word.index("g"))  # 6
print("capatalize -> ",A_Word.capitalize())  # Program on a specified delimiter