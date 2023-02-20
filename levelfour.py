# In level four, give the user an option
# 1) to play against the computer or to
# 2) think of a number for the computer to guess.

chooseGame = input("Please pick a game option a or b:")

if chooseGame == 'a':
    exec(open('./levelone.py').read())
    # Open the .py file at a specific location. And then read(). Then execute.
elif chooseGame == 'b':
    exec(open('./leveltwo.py').read())
else:
    print('You did not choose a valid game option.')
