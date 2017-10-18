import menu
import game

menu.splash()
menuOption = menu.mainMenu()
if menuOption == 1:
    game.newGame(1,1,1)
elif menuOption == 2:
    menu.options()
    pass
elif menuOption == 3:
    quit()
