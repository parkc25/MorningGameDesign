#Christan Park 
#Make a list of at least 10 words
#Randomly select a word
#ask the user to guess the word (give a hint about what kind of words you are using: fruits, animals,etc)
#If they guess right congratulate them if mot say sorry "you missed"
from operator import truediv
import os
import random

from pygame import KMOD_SHIFT, K_h
os.system('cls')

#Game with Unlimited Guesses 
#make game pretty, tell them what it is about, and how to play

all_games=True
while all_games:
    print("***************************************************************************") 
    print("") 
    print("Welcome!")
    name = input("What is your name? ")
    print("Hi",name,", here are the rules:")
    print("Pick a game below and play it!")
    print("1. Guess the Number")
    print("2. Guess the Fruit")
    print("3. Guess the Animal")
    print("Good Luck " + name + "!")
    print("")
    print("***************************************************************************")
    print("")
    while True: 
        choice = input("What game do you want to play? 1, 2, or 3? ")
        print("")
        try:
            choice=int(choice)
            if choice == 1:
                number_game = True
                while number_game:
                    print("***************************************************************************") 
                    print("") 
                    print("Welcome to Guess The Number!")
                    print("Hi",name,", here are the rules:")
                    print("1. Guess a number from 0 to 50")
                    print("2. You have 5 guesses")
                    print("3. After each incorrect guess you will recieve a hint of lower or higher")
                    print("Good Luck",name,"!")
                    print("")
                    print("***************************************************************************")
                    print("")

                    random_number = random.randint(1,50) #allows computer to choose a number between 1 and 50
                    number_of_guesses = 0
                    #print("The random number is", random_number)

                    while number_of_guesses < 5: #makes user limited to 5 guesses
                        guess = int(input("Guess a number: ")) #make into int to allow it to be on the same line as a number
                        number_of_guesses += 1
                        if guess < random_number:
                            print('The random number is higher')
                        if guess > random_number:
                            print('The random number is lower')
                        if guess == random_number:
                            break
                    print("")
                    if guess == random_number:
                        print("You guessed the number! The number was " + str(random_number) + "!") #make number string to allow to be on the same line as letters
                    else:
                        print('Sorry, you did not guess the number. The number was ' + str(random_number) + ".")
                    print("")
                    print("***************************************************************************")
                    print("")
                    print("Thank you for playing! ")
                    print("Would you like to play the number game again, choose a new game. or not play at all? ")
                    print("To play the number game again type 'number game'")
                    print("To play another game type 'new game'")
                    print("To stop playing type 'stop'")
                    play_again = input("Type your response here: ")
                    if play_again == "number game" or "Number game" or "Number Game": 
                        number_game=True
                        print("")
                    elif play_again == "new game" or "New game" or "New Game": 
                        all_game=True
                        print("")
                    else:
                        print("Ok, see you later and thank you for playing!")
                        number_game = False
                        print("")
                        print("***************************************************************************")
            elif choice == 2:
                Ksjd
            elif choice == 3:
                jjh
            else:
                print("Sorry we don't have that game please choose from 1, 2, or 3!")
        except:
            print("Sorry we don't have that game please choose from 1, 2, or 3!")

