v = 2
s = 2
if v == s:
    print(f"Equal -> {v == s}",)
else:
    print("Not Equal")
v = s = 2
if v != s:
    print(f"Equal",)
else:
    print(f"Not Equal -> {v != s}")
v = 5
s = 3
if v > s:
    print(f"v is greater -> {v > s}",)
else:
    print(f"s is greater -> {v < s}")
v = 5
s = 8
if v > s:
    print(f"v is greater -> {v > s}",)
else:
    print(f"s is greater -> {v < s}")
v = 2
s = 12
if v < s:
    print(f"v is smaller -> {v < s}",)
else:
    print(f"s is smaller -> {v > s}")
v = 22
s = 12
if v < s:
    print(f"v is smaller -> {v < s}",)
else:
    print(f"s is smaller -> {v > s}")
v = 22
s = 12
if v >= s:
    print(f"v is greater -> {v > s}",)
else:
    print(f"s is greater -> {v < s}")
v = 12
s = 22
if v <= s:
    print(f"v is smaller -> {v < s}",)
else:
    print(f"s is smaller -> {v > s}")


