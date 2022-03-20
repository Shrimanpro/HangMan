from random import *

print("Welcome to moi game. You have 5 chances to find out the secret word.");

wordList = "Joel", "Sean", "Rishi", "Anish", "Soham", "Kshrugal", "Amogh";
secret = choice(wordList);

guessed = False;
hangMan = ['_'] * len(secret)
letters = []
life = 5

while (guessed is False):
    print("Word:", hangMan)
    print("Guessed Letters:", letters)
    print("Lives:", life)
    if (life <= 0):
        print("haha trash")
        break
    x = input("Guess? ")
    
    if (len(x) == 1):
        letters.append(x)
        if (x in secret.casefold()):
            print("Nice")
            ind = secret.casefold().index(x)
            hangMan[ind] = secret[ind:ind + 1]
            
        else:
            life -= 1
            print("Wrong")
            
    elif (x == secret.casefold()):
        print("wow, u got lucky")
        guessed = True
        
    else:
        print("Wrong")
        life -= 1
        
    if (not("_" in hangMan)):
        guessed = True
        print("Congrats you won")

        
