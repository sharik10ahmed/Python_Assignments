v1 = 10
v1 = v1 + v1
print("1 Plus->",v1)
v1 += v1
print("2 PLus->",v1)
v1 *= v1
print("3 Multi ->",v1)
import sys

# Set a new, higher limit for integer string conversion.
# Choose a number larger than the number of digits in your integer (v1).
new_limit = 9000  # Example: 5000 digits

sys.set_int_max_str_digits(new_limit)

# Now, your code will run without the ValueError
v1 **= v1
print("4 Exponential ->",v1)
v1 /= v1
print("4 Division->",v1)
v1 %=v1
print("5 Modulo or Modular->",v1)
v1 -= v1
print("6 Diff->",v1)

