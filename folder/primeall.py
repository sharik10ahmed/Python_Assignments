print("Prime numbers between 1 and 100 are:")

# Loop through the numbers from 2 to 100
for num in range(2, 101):
    is_prime = True
    
    # Check if the number is divisible by any number other than 1 and itself
    for i in range(2, num):
        if num % i == 0:
            is_prime = False # We found a factor, so it's not prime
            break            # Stop checking further factors for this number
            
    # If the flag is still True, the number is prime
    if is_prime:
        # print the number on the same line, separated by a space
        print(num, end=" ")