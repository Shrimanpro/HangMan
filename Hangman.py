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
        test = secret
        if (x in test.casefold()):
            y = 0
            ''' I made test a copy of secret and made a int variable to keep track how many
                times it went through
                Since I removed letters from "test", I added y to the index for the hangman variable to match up
                Finally to close the loop I incremented y by 1 
            '''
            while (x in test.casefold()):
                index = test.casefold().index(x)
                hangman[index + y] = test[index:index + 1]
                test = test[0:index] + test[index + 1:len(test)]
                y = y + 1
            print("Nice")
        else:
            life -= 1
            print("Wrong")
    
    # This will see if your guess is the actual word
    # if it is, it'll update the guessed variable  
    elif (x == secret.casefold()):
        print("Final Word:", secret)
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
        print("Final Word:", secret)
        print("Congrats you won")

        
