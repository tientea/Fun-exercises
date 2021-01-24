def reverse_sentence():
    user = str(input("Give me a sentence: "))
#Deals with situations when a conjoined sentence is given
    if " " in user:
     user = user.split()
     user = " ".join(user[::-1])
     print(user)
    else:
     print("Please add spaces to your sentence")
     reverse_sentence()
    
reverse_sentence()