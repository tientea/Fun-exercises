def reverse_highlow():
    min_num = 0
    max_num = 100
    guess = 1
    bot_answer = 50
    print("Please guess a number in your head")
    condition = input("Is your guess " + str(bot_answer) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high) ")
    while condition != 1:
       guess += 1
       if condition == 0:
           min_num = bot_answer + 1
       elif condition == 2:
           max_num = bot_answer - 1
       bot_answer = (min_num + max_num) / 2
       condition = input("Is your guess " + str(bot_answer) + "? (0 means it's too low, 1 means it's your guess and 2 means it's too high) ")
       print("It took" , guess , "times to guess your number")
reverse_highlow()