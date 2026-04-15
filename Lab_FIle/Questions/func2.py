# Function Definition with a default parameter
def greet(name, message="Hello"):
    print(message, name)

# 1. Calling WITHOUT the second argument (uses default)
greet("Alice") 

# 2. Calling WITH the second argument (overwrites default)
greet("Bob", "Good morning")