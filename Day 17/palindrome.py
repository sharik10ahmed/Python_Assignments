palindromes = ["word","bob","civic","level"]
for word in palindromes:
  reverse = word[::-1]
  if word.lower() == reverse.lower() :
    print(f"{word} -> Your are dealing with a palindrome word")
  else:
    print(f"{word} -> NO its not")