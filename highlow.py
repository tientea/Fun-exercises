import random


def high_low():
 count = 0
 a = random.randint(1, 9)
 user = int(input("Please enter a number from one to nine: "))
 while True :
#definitely can simplify the user input condition
  if user > a and user >= 1 and user <=9:
         print("Lower")
         user = int(input("Please enter a different number: "))
         count += 1
  elif user < a and user >= 1 and user <=9: 
         print("Higher")
         user = int(input("Please enter a different number: "))
         count += 1
  elif user == a:
         print("You've won, you took", count, "try/tries to win!")
         ans = input("Would you like to play again? Y/N")
         if ans == "y":
           high_low()
         else:
           print("Thank you for playing!")
           break
# there seems to be a problem when you try to stop after playing multiple times
  else:
         user = int(input("Please enter a valid answer:"))

                  
high_low()