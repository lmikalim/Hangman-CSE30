# assignment: Hangman(Programming Assignment 1)
# author: Mika Lim
# date: Sept 30 2022 
# file: hangman.py is a program that simulates a hangman word guessing game
# input: file 'dictionary_short.txt'
# output: None

from curses.ascii import isdigit
import random


dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located


def import_dictionary (filename) :
    dictionary = {}
    
    max_size = 12
   
    d = open('dictionary-short.txt', "r")
    for x in d:
       if x != '':
        wordLength = len(x.strip())
        if wordLength in dictionary:
            currentVal = dictionary[wordLength]
            currentVal.append(x.strip())
            dictionary[wordLength] = currentVal
        else:
                print('adding',x.strip(),'to dictionary at',wordLength)
                dictionary[wordLength] = [x.strip()]
    d.close()
    print(dictionary)
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    for i in dictionary:
        print(i)
    return

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options ():
    lives = 5
    wordSize = random.randint(3,12)
    ##WORD LENGTH SETUP
    print("Please choose a size of a word to be guessed [3 - 12, default any size]:")
    
    lives = 5
    validNums = [3,4,5,6,7,8,9,10,11,12]
    wordSize = random.randint(3,12)
    try:
        val  = input()
        if val.isdigit():
            if int(val) in validNums:
                    wordSize = int(val)
    except:
        wordSize = random.randint(3,12)
    
    print('The word size is set to',wordSize,'.')

    ## LIVES SETUP
    print('Please choose a number of lives [1 - 10, default 5]:')
    validLives = [1,2,3,4,5,6,7,8,9,10]
    try:
        val2 = input()
        if val2.isdigit():
            if int(val2) in validLives:
                    lives = int(val2)
            else:
                    lives = 5
    except:
        lives = 5
    print("You have ",lives," lives.")
    
    return(wordSize,lives)


def generate_secret_word(wordSize):
     return random.choice(dictionary[wordSize])

def generate_public_word(wordSize,word):
    publicWord = []
    for i in range(wordSize):
        if word[i] == '-':
            publicWord.append('-')
            continue
        publicWord.append('__' )
    return publicWord

def update_public_word(currentWord, secretWord, newLetter):
    print("update public word")
    secretWord = secretWord.upper()
    newLetter = newLetter.upper()
    for i in range(len(secretWord)):
        if secretWord[i] == newLetter and secretWord[i] != '-':
            currentWord[i] = newLetter.upper()
    print(*currentWord, sep=" ")

def createLivesVisualizer(numLives):
    livesVis = ''
    for i in range(lives):
        livesVis = livesVis + '0'
    return livesVis

def updateLives(livesVisualizer,livesLeft):
    newLives = [*livesVisualizer]
    Xnums = len(livesVisualizer) - livesLeft
    if 'X' not in livesVisualizer:
        newLives[0] = 'X'
    else:   
        for i in range(len(livesVisualizer)):
            if Xnums > 0:
                newLives[i] = 'X'
                Xnums = Xnums - 1
            
  
    return newLives


if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print a game introduction
    print("Welcome to the Hangman Game!")
    isPlaying = True
    gameRunning = False
    # START MAIN LOOP (OUTER PROGRAM LOOP)

    while isPlaying == True:
     

        # ##WORD LENGTH SETUP
        # print("Please choose a size of a word to be guessed [3 - 12, default any size]:")
        # val  = input()
        # lives = 5
        # validNums = [3,4,5,6,7,8,9,10,11,12]
        # wordSize = random.randint(3,12)
        # if val.isdigit():
        #     if int(val) in validNums:
        #         wordSize = int(val)
        # else:
        #         wordSize = random.randint(3,12)
        # print('The word size is set to',wordSize,'.')
        wordSize,lives = get_game_options()
        secretWord = generate_secret_word(wordSize)
        publicWord = generate_public_word(wordSize,secretWord)


        # ## LIVES SETUP
        # print('Please choose a number of lives [1 - 10, default 5]:')
        # val2 = input()
        # validLives = [1,2,3,4,5,6,7,8,9,10]
        # if val2 == '':
        #     lives = 5
        # elif val2.isdigit():
        #     if val2.isdigit() in validLives:
        #         lives = int(val2)
        #     else:
        #         lives = 5
        # print("You have ",lives," lives.")
        livesVisualizer = createLivesVisualizer(lives)
     

        ##GAME BEGINS
        lettersChosen = []
        gameRunning = True
        while gameRunning == True:
            
            print("Letters chosen:", *lettersChosen)
            print(*publicWord,"lives:",lives, end =" ")
            print( *livesVisualizer,sep='')

            print("Please choose a new letter > ")

            inputLetter = input()
            if inputLetter.upper() in lettersChosen:
                print("You have already chosen this letter")
                continue
        

            ## CHECK LETTER IN WORD
            if inputLetter in secretWord:
                print(update_public_word(publicWord,secretWord,inputLetter))
                lettersChosen.append(inputLetter.upper())
            else:
                lives = lives - 1
                livesVisualizer = updateLives(livesVisualizer,lives)
                lettersChosen.append(inputLetter.upper())

            if lives == 0:
                print("You lost! The word is",secretWord.upper(),"!")
                gameRunning = False
            elif '__' not in publicWord:
                print("Congratulations!!! You won! The word is",secretWord.upper(),"!")
                gameRunning = False
        
        print("Would you like to play again [Y/N]?")
        answer = input()
        if answer.upper() == "Y":
            isPlaying = True
        elif answer.upper() == "N":
            print("Goodbye!")
            isPlaying = False

        
        


    

 