x = "I am Global" # Global Scope

def my_function():
    y = "I am Local" # Local Scope
    print(y)
    print(x) # Can see Global x

my_function()

print(y) # <-- This would cause an ERROR because y 'died' when the function ended.