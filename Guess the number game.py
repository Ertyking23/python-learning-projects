import random

print("===GUESS THE NUMBER GAME (1 to 20)===")
startgame = input("Start the game? (Y/N): ").upper()
numbers = list(range(1, 21))
rightnumber = random.choice(numbers)
guesses = 0
game_over = False

def gamelogic():
    global guesses, game_over
    if guesses >= 5 or game_over:
        return
        
    try:
        numberguessed = int(input("Choose a number (1-20): "))
        if numberguessed < 1 or numberguessed > 20:
            print("Please enter a number between 1-20!")
            return gamelogic()
    except ValueError:
        print("Please enter a valid number!")
        return gamelogic()
        
    levelofguess = numberguessed - rightnumber
    guesses += 1
    
    if levelofguess == 0:
        print("You won!")
        game_over = True
    elif abs(levelofguess) == 1:
        print("You almost got it!")
    elif abs(levelofguess) == 2:
        print("You're getting there")
    elif abs(levelofguess) == 3:
        print("Wrong")
    else:
        print("You got it terribly wrong")
        
    if guesses >= 5 and not game_over:
        gameover()
    elif not game_over:
        gamelogic()

def gameover():
    print("You've reached the maximum of 5 guesses")
    retry = input("Try again? (Y/N): ").upper()
    if retry == "Y":
        global guesses, rightnumber, game_over
        guesses = 0
        rightnumber = random.choice(numbers)
        game_over = False
        gamelogic()
    else:
        print("Goodbye")

if startgame == "Y":
    gamelogic() 
elif startgame == "N":
    print("Okay, have a nice day!")
else:
    print("Please type either Y or N")