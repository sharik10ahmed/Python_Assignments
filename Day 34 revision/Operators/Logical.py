v = 10
s = 20
if v+10 == s and s-10 == v :
    print(f"Conditions are True = {v and s}",)
else:
    print(f"Conditions are False = {v and s}")
v = 10
s = 20
if v+10 == s or s-50 == v :
    print(f"Only 1 Condition is true = {v or s}",)
else:
    print(f"Conditions are False = {v or s}")
v = s = 5
if not(v+s==20) :  # becomes true because of not
    print(f"{not(v==s)}",)  # enters in if block and in print it converts v==s which is true to false so output is false
else:
    print(f"{not(v!=s)}")
        