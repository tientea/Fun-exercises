import string
import random

def pass_gen():
    user  = input("Determine the strength of your password:(strong/weak) ")
    if user == "strong":
     letters = string.ascii_letters
     symbols = string.punctuation
     numbers = string.digits
     password = letters + symbols + numbers
     print( "".join(random.choice((password)) for i in range(10)))
    else:
     password = random.sample(("aaa","bbb","ccc"),2)
     print("".join(password))
    
pass_gen()
