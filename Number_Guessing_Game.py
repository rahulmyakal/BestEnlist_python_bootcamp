import random
guess = random.randint(1,100)
Guesses = 0
UserGuess = None

while UserGuess != guess:
    UserGuess = int(input("Enter the Number to Guess \n "))

    if guess == UserGuess:
        print(f"You Guessed the right Number")
    else:
        Guesses = Guesses + 1

        if guess>UserGuess:
            print(f"Enter thr number Larger of this Number")
        else:
            print(f"Enter the number Smaller of this Number")

print(f"You guess the correct number in {Guesses} Guesses")