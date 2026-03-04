winning_num = 7
guess = 0

while guess != winning_num:
    guess = int(input("Guess the no.->  "))
    if guess < winning_num:
        print("Too low!")
    elif guess > winning_num:
        print("Too high!")

print("You won!")