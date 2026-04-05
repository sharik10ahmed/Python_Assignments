def is_prime(number):
    # Step 1: Prime numbers must be greater than 1
    if number <= 1:
        return False
        
    # Step 2: Try dividing the number by everything from 2 up to (number - 1)
    for i in range(2, number):
        # The '%' operator gives us the remainder of a division.
        # If the remainder is 0, it means 'i' is a factor.
        if number % i == 0:
            return False # We found a factor, so it's NOT prime
            
    # Step 3: If the loop finishes and we found no factors, it IS prime
    return True

# --- Testing the code ---
test_number = int(input("Enter a no.-> "))

if is_prime(test_number):
    print(test_number, "is a Prime Number")
else:
    print(test_number, "is Not a Prime Number")