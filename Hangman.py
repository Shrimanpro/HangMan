from random import *


print("Welcome to moi game. You have 5 chances to find out the secret word.");

#Makes a word list that it randomly picks from
word_list = "Joel", "Sean", "Rishi", "Anish", "Soham", "Kshrugal", "Amogh";
secret = choice(word_list);

#Made some variables for the while loop and for the output
guessed = False;
hangman = ['_'] * len(secret)
letters = []
life = 5

#Keeps running the while loop until the variable turns true
while (guessed is False):
    print("Word:", hangman)
    print("Guessed Letters:", letters)
    print("Lives:", life)
    #This if statement sees if you have 0 lives and if you do it ends the game
    if (life <= 0):
        print("haha trash")
        break
    x = input("Guess? ")
    
    '''This if statement will see the input
        and if its 1 char long it'll see if it's in the word
        if it is it'll update the hangman array
        if its not there then it'll subtract a life
    '''
    if (len(x) == 1):
        letters.append(x)
        if (x in secret.casefold()):
            print("Nice")
            index = secret.casefold().index(x)
            hangman[index] = secret[index:index + 1]
            
        else:
            life -= 1
            print("Wrong")
    
    # This will see if your guess is the actual word
    # if it is, it'll update the guessed variable  
    elif (x == secret.casefold()):
        print("wow, u got lucky")
        guessed = True
        
    #If whatever the user inputs is not in the word
    # it'll subtract a life   
    else:
        print("Wrong")
        life -= 1
    
    # This finally sees if there is any empty spaces in the array
    # if there isn't then it'll update guessed and end the loop
    if (not("_" in hangman)):
        guessed = True
        print("Congrats you won")

        
