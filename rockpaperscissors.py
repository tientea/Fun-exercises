#rock paper scissor

def gameover():
   while True:
    ans = input("Would you like to play again y/n:")
    if ans == "n":
       break
    else:
        rockpaperscissors()

def rockpaperscissors():
    x = input("What is your play?(rock/paper/scissors)")
    y = input("What is your play(rock/paper/scissors)")
    if x == "rock":
            if y == "rock":
                print("draw")
                gameover()
            if y == "paper":
                print("player two wins")
                gameover()
            if y == "scissors":
                print("player one wins")
                gameover()
    elif x == "paper":
            if y == "rock":
                print("player one wins")
                gameover()
            if y == "paper":
                print("draw")
                gameover()
            if y == "scissors":
                print("player two wins")
                gameover()
    elif x == "scissors":
            if y == "rock":
                print("player two wins")
                gameover()
            if y == "paper":
                print("player one wins")
                gameover()
            if y == "scissors":
                print("draw")
                gameover()
    else:
        print("Please input a valid play (rock/paper/scissors)")
        rockpaperscissors()
rockpaperscissors()