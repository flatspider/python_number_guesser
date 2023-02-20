import random

moves = ['rock', 'paper', 'scissors']

play = True
# A list is created by [] and is mutable.

# A tuple is established by ().

while play == True:
    player = input("Rock, Paper, Scissors? ").lower()
    print(player)
    if player not in moves:
        print("That is not a valid choice.")
        continue

    computer = random.choice(moves)

    print("computer:", computer)

    if player == computer:
        print("It's a tie!")
        continue
    elif player == 'rock':
        if computer == 'paper':
            print("You lose.", computer.capitalize(), "covers", player, "!")
        else:
            print("You win!", player.capitalize(), "smashes", computer, "!")
    elif player == 'paper':
        if computer == 'scissors':
            print("You lose.", computer.capitalize(), "slices", player, "!")
        else:
            print("You win!", player.capitalize(), "covers", computer, "!")
    elif player == 'scissors':
        if computer == 'rock':
            print("You lose.", computer.capitalize(), "smashes", player, "!")
        else:
            print("You win!", player.capitalize(), "slices", computer, "!")

    play = False
