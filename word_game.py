# Simple Word Game.
# Created by: Luiz Gabriel Magalhães Trindade.
# Distributed under the GPL3 License: https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

from random import choice, shuffle                      #Modules to import.

print("""
-----------------------
SIMPLE WORD GUESS GAME!
-----------------------
-If you wanna give up 
type: igiveup

-If you wanna give up, 
but wanna keep playing, 
type: nextword
-----------------------
""")

words = []                                              #Initialization of the list os words.
with open("portuguese.txt", "r") as file:               #Open the file with words to guess.
    words = [line.strip() for line in file]             #Using list comprehension to store all the values.

word = choice(words)                                    #Chose the word to guess.

def Shuffle_Word():
    word_to_try = list(word)                            #Shuffle the word.
    shuffle(word_to_try)
    word_to_try = ''.join(word_to_try)
    print(word_to_try)                                  #Print in the screen the word shuffled.
Shuffle_Word()

trys = int(0)                                           #Trys.
while True:                                             #While True for running the game.
    user_try = input("Guess the word!: ")               #The user try to guess the word.
    
    if user_try == word:                                #If the word is correct the player win.
        print("Well done!")
        word = choice(words)
        trys = 0
    elif user_try == "igiveup":                         #If the player wants to give up.
        print(f"Correct word: {word}")
        break
    elif user_try == "nextword":                        #If the palyer give up but want to keep playing.
        word = choice(words)
        Shuffle_Word()
        trys = 0
    else:                                               #If the player guess is wrong, the 'trys' add 1.
        trys += 1
        print(f"Trys: {trys}")
