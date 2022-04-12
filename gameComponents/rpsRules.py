from random import randint
from gameComponents import winLose, gameVars
from colored import fore, back, style

def rps(status):

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