import random

def compare_num(digits, user_answer):
    cowbull=[0,0]
    for i in range(len(digits)):
        if digits[i] == user_answer[i]:
            cowbull[0] += 1
        else:
            cowbull[1] += 1
    return cowbull
            
if __name__ == "__main__":
    playing = True
    digits = str(random.randint(0,9999))
    guesses = 0
    
    while playing:
        user_answer = input("Give me a four digit number")
        if user_answer == "exit":
            break
        cowbullcount = compare_num(digits, user_answer)
        guesses += 1
        
        print("There are " + str(cowbullcount[0])+ " cows and " + str(cowbullcount[1]) + "bulls.")
        
        if cowbullcount[1] == 4:
            playing = False
            print("You've won! You took ", guesses, " guess(s).The number was ", digits)
            break
        else:
            print("Try again")
