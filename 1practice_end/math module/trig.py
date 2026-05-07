import math

print("--- TRIGONOMETRIC FUNCTIONS ---")
# Important Note: Python's math.sin, math.cos, and math.tan expect 
# the angle to be in RADIANS, not degrees.
# To make it easier to understand, we will convert 45 degrees to radians first.

angle_in_degrees = 45
angle_in_radians = math.radians(angle_in_degrees)

print(f"Angle: {angle_in_degrees} degrees")

# 1. Sine
sine_value = math.sin(angle_in_radians)
print(f"math.sin({angle_in_radians:.4f}) = {sine_value:.4f}")

# 2. Cosine
cosine_value = math.cos(angle_in_radians)
print(f"math.cos({angle_in_radians:.4f}) = {cosine_value:.4f}")

# 3. Tangent
tangent_value = math.tan(angle_in_radians)
print(f"math.tan({angle_in_radians:.4f}) = {tangent_value:.4f}")


print("\n--- LOGARITHMS ---")
# Let's use the number 100 for our logarithm examples
number = 100
print(f"Target Number: {number}")

# 4. Natural Logarithm (base 'e', where 'e' is approx 2.718)
# This asks: "e to what power equals 100?"
nat_log = math.log(number)
print(f"math.log({number})   = {nat_log:.4f}")

# 5. Base-10 Logarithm
# This asks: "10 to what power equals 100?" (The answer should be exactly 2)
base10_log = math.log10(number)
print(f"math.log10({number}) = {base10_log}")