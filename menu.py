import extra

menuOptions = ['1. New Game', '2. Options', '3. Quit']

def splash():
    print("\n\n")
    print("Return to Civilization by Emerald")
    print("\n")
    print("########  ######## ######## ##     ## ########  ##    ## ")
    print("##     ## ##          ##    ##     ## ##     ## ###   ## ")
    print("##     ## ##          ##    ##     ## ##     ## ####  ## ")
    print("########  ######      ##    ##     ## ########  ## ## ## ")
    print("##   ##   ##          ##    ##     ## ##   ##   ##  #### ")
    print("##    ##  ##          ##    ##     ## ##    ##  ##   ### ")
    print("##     ## ########    ##     #######  ##     ## ##    ## ")
    print("\n")
    print("########  ####### ")
    print("   ##    ##     ## ")
    print("   ##    ##     ## ")
    print("   ##    ##     ## ")
    print("   ##    ##     ## ")
    print("   ##    ##     ## ")
    print("   ##     #######  ")
    print("\n")
    print(" ######  #### ##     ## #### ##       #### ########    ###    ######## ####  #######  ##    ## ")
    print("##    ##  ##  ##     ##  ##  ##        ##       ##    ## ##      ##     ##  ##     ## ###   ## ")
    print("##        ##  ##     ##  ##  ##        ##      ##    ##   ##     ##     ##  ##     ## ####  ## ")
    print("##        ##  ##     ##  ##  ##        ##     ##    ##     ##    ##     ##  ##     ## ## ## ## ")
    print("##        ##   ##   ##   ##  ##        ##    ##     #########    ##     ##  ##     ## ##  #### ")
    print("##    ##  ##    ## ##    ##  ##        ##   ##      ##     ##    ##     ##  ##     ## ##   ### ")
    print(" ######  ####    ###    #### ######## #### ######## ##     ##    ##    ####  #######  ##    ## ")
    print("\n")

def mainMenu():
    print("Main Menu")
    for line in menuOptions:
        print(line)
    while True:
        option = input('Select an option: ')
        if extra.isInt(option) != True or int(option) > len(menuOptions):
            pass
        else:
            return int(option)

def options():
    pass
