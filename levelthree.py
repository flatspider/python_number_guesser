from random import randint

guessCounter = 0
playOn = 1

# The computer will guess until it is correct
# while computerGuess != playerNumber

print("Player, think of a number between 1 and 10.")

computerGuess = randint(1, 10)
maxGuess = 11
minGuess = 1

while playOn > 0:
    guessCounter += 1
    print("My guess is", computerGuess)
    playersInput = input(
        "Was that too high, too low or was I correct? h/l/c: ")
    if playersInput == 'c':
        print("Computer wins in", guessCounter, "guesses")
        break
    elif playersInput == 'h':
        print("high")
        maxGuess = computerGuess
        # Integer division // and if it was too low, add to that guess.
        # Then take the last guess, and move to lower halfway point
        # Update the max guess when you are too high.
    elif playersInput == 'l':
        print("low")
        minGuess = computerGuess
        # This does not work for the number 6.
        # Then take the last guess 5, and move to the upper halfway point
        # within the available range
        # Update the low guess when you are too low.
    computerGuess = minGuess + (maxGuess - minGuess) // 2

print("Game over.")
