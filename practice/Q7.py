num = int(input("enter a no.-> "))
total = 0

for digit in str(num):
    total += int(digit) ** 3  # Cubes the digit

if total == num:
    print("Armstrong")
else:
    print("Not Armstrong")