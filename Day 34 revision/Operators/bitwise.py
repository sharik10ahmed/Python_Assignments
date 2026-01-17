First = 10  # 1010 in binary
Second = 4   # 0100 in binary
result_and = First & Second
print(f"10 & 4 = {result_and}") # Output: 0

a = 10  # 1010 in binary
b = 4   # 0100 in binary
result_or = First | Second
print(f"10 | 4 = {result_or}")  # Output: 14

a = 10  # 1010 in binary
b = 4   # 0100 in binary
result_xor = First ^ Second
print(f"10 ^ 4 = {result_xor}") # Output: 14

First = 10
result_not = ~First
print(f"~10 = {result_not}") # Output: -11