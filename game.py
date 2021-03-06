from random import randint
from gameComponents import winLose, gameVars
from gameComponents import rpsRules
from colored import fore, back, style



print(fore.DARK_ORANGE_3A + ' ==============!! ROCK, PAPER, SCISSORS !!======================== ')
print()

while gameVars.player is False:

    gameVars.player = input(fore.BLACK + back.INDIAN_RED_1A + "Choose your weapon:" + fore.LIGHT_GRAY + "rock, paper, scissors: " + style.RESET)
    gameVars.computer = gameVars.choices[randint(0, 2)]

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)

    if (gameVars.computer == gameVars.player):
        print(fore.RED_3A + back.LIGHT_GRAY + "tie! try again!" + style.RESET)

    elif (gameVars.player == "rock"):
        if (gameVars.computer == "paper"):
            print(fore.RED_3A + "you lose!" + style.RESET)
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print(fore.CYAN + "you win!" + style.RESET)
            gameVars.computerLives = gameVars.computerLives - 1

    elif (gameVars.player == "paper"):
        if (gameVars.computer == "scissors"):
            print(fore.RED_3A + "you lose!" + style.RESET)
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print(fore.CYAN + "you win!" + style.RESET)
            gameVars.computerLives = gameVars.computerLives - 1

    elif (gameVars.player == "scissors"):
        if (gameVars.computer == "rock"):
            print(fore.RED_3A + "you lose!" + style.RESET)
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print(fore.CYAN + "you win!" + style.RESET)
            gameVars.computerLives = gameVars.computerLives - 1

    print(fore.YELLOW + "computer life count: " + str(gameVars.computerLives))
    print(fore.YELLOW + "player life count: " + str(gameVars.playerLives))

    if gameVars.playerLives == 0:
        # call the winorlose function here
        winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
        # call the winorlose function here
        winLose.winorlose("won")

    gameVars.player = False