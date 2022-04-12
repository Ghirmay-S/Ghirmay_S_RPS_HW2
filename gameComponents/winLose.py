from gameComponents import gameVars
from gameComponents import rpsRules
from colored import fore, back, style

def winorlose(status):


    print(fore.MEDIUM_VIOLET_RED + "You " + status + "! Would you like to play again?" + style.RESET)

    choice = input(fore.SKY_BLUE_2 + " Y / N? ")

    if choice == "n":
        print(fore.CYAN + "better luck next time!")
        exit()
    elif choice == "y":
        gameVars.layerLives = 5
        gameVars.computerLives = 5
        gameVars.player = False