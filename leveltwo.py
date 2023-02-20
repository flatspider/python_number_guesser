from random import randint

counter = 3


options = ['Higher', 'Lower', 'Correct']

while counter > 0:
    computer = randint(1, 10)
    print("My guess is", computer)
    playersInput = input("Was I right? y/n: ")
    if playersInput == 'y':
        print("Computer wins!")
        break

    counter -= 1

print("Game over.")
