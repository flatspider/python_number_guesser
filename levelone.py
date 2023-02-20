from random import randint

computer = randint(1, 10)

counter = 3

while counter > 0:
    playerGuess = int(input("Guess a number in between 1 and 10: "))
    if playerGuess == computer:
        print("You win!")
        break
    elif playerGuess > computer:
        print("Too high of a guess!")
    else:
        print("Too low of a guess!")

    counter -= 1

if playerGuess != computer:
    print("You lose. The number was", computer)
