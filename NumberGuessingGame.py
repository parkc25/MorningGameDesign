#Christan Park 
#Make a list of at least 10 words
#Randomly select a word
#ask the user to guess the word (give a hint about what kind of words you are using: fruits, animals,etc)
#If they guess right congratulate them if mot say sorry "you missed"
from datetime import date, datetime
from operator import truediv
import os, datetime
import random
import sys
date = datetime.datetime.now()


from pygame import KMOD_SHIFT, K_h
os.system('cls')

#Game with Unlimited Guesses 
#make game pretty, tell them what it is about, and how to play

start_game = True
while start_game:
    print("***************************************************************************") 
    print("") 
    print("Welcome ot Guess a Number!")
    name = input("What is your name? ")
    print("Hi",name,", here are the rules:")
    print("There are three levels to this game")
    print("Pikc a level and have fun!")
    print("1. Guessing from 1-25")
    print("2. Guessing from 1-50")
    print("3. GUessing from 1-100")
    print("Good Luck " + name + "!")
    print("")
    print("***************************************************************************")
    print("")
    all_games = True
    while all_games:
        high = 0
        while True:
            answer = input("Would you like to play? ")
            if "no" in answer:
                print("See you next time!")
                sys.exit()
            choice = input("What game do you want to play? 1, 2, or 3? ")
            choice=int(choice)
            if choice == 1:
                number_game = True
                while number_game:
                    print("***************************************************************************") 
                    print("") 
                    print("Welcome to Guess a Number from 1-25!")
                    print("Hi",name,", here are the rules:")
                    print("1. Guess a number from 1 to 25")
                    print("2. You have 5 guesses")
                    print("3. After each incorrect guess you will recieve a hint of lower or higher")
                    print("Good Luck",name,"!")
                    print("")
                    print("***************************************************************************")
                    print("")

                    random_number = random.randint(1,25) #allows computer to choose a number between 1 and 50
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
                    print("Thank you for playing! You guessed it in "+ str(number_of_guesses) + " tries!")
                    print("Would you like to play the number game again, choose a new game. or not play at all? ")
                    print("To play the number game again type '1'")
                    print("To play another game type or stop playing '2'")
                    play_again = int(input("Type your response here: "))
                    if play_again == 1: 
                        number_game=True
                        print("")
                    elif play_again == 2:
                        print("Follow the instructions below to continue playing!")
                        all_games = False
                        number_game = False
                        print("")
                        print("***************************************************************************")
                    else:
                        print("Ok, see you later and thank you for playing!")
                        all_games = False
                        number_game = False
                        print("")
                        print("***************************************************************************")
            elif choice == 2:
                number_game = True
                while number_game:
                    print("***************************************************************************") 
                    print("") 
                    print("Welcome to Guess a Number from 1-50!")
                    print("Hi",name,", here are the rules:")
                    print("1. Guess a number from 1 to 50")
                    print("2. You have 8 guesses")
                    print("3. After each incorrect guess you will recieve a hint of lower or higher")
                    print("Good Luck",name,"!")
                    print("")
                    print("***************************************************************************")
                    print("")

                    random_number = random.randint(1,50) #allows computer to choose a number between 1 and 50
                    number_of_guesses = 0
                    #print("The random number is", random_number)

                    while number_of_guesses < 8: #makes user limited to 5 guesses
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
                    print("Thank you for playing! You guessed it in "+ str(number_of_guesses) + " tries!")
                    print("Would you like to play the number game again, choose a new game. or not play at all? ")
                    print("To play the number game again type '1'")
                    print("To play another game type or stop playing '2'")
                    play_again = int(input("Type your response here: "))
                    if play_again == 1: 
                        number_game=True
                        print("")
                    elif play_again == 2:
                        print("Follow the instructions below to continue playing!")
                        all_games = False
                        number_game = False
                        print("")
                        print("***************************************************************************")
                    else:
                        print("Ok, see you later and thank you for playing!")
                        all_games = False
                        number_game = False
                        print("")
                        print("***************************************************************************")
            elif choice == 3:
                number_game = True
                while number_game:
                    print("***************************************************************************") 
                    print("") 
                    print("Welcome to Guess a Number from 1-100!")
                    print("Hi",name,", here are the rules:")
                    print("1. Guess a number from 1 to 100")
                    print("2. You have 10 guesses")
                    print("3. After each incorrect guess you will recieve a hint of lower or higher")
                    print("Good Luck",name,"!")
                    print("")
                    print("***************************************************************************")
                    print("")

                    random_number = random.randint(1,100) #allows computer to choose a number between 1 and 50
                    number_of_guesses = 0
                    #print("The random number is", random_number)

                    while number_of_guesses < 10: #makes user limited to 5 guesses
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
                    print("Thank you for playing! You guessed it in "+ str(number_of_guesses) + " tries!")
                    print("Would you like to play the number game again, choose a new game. or not play at all? ")
                    print("To play the number game again type '1'")
                    print("To play another game type or stop playing '2'")
                    play_again = int(input("Type your response here: "))
                    if play_again == 1: 
                        number_game=True
                        print("")
                    elif play_again == 2:
                        print("Follow the instructions below to continue playing!")
                        all_games = False
                        number_game = False
                        print("")
                        print("***************************************************************************")
                    else:
                        print("Ok, see you later and thank you for playing!")
                        all_games = False
                        number_game = False
                        print("")
                        print("***************************************************************************")
            else:
                print("Sorry we don't have that game please choose from 1, 2, or 3!")
            score= 2000-40*number_of_guesses 
            if score > high:
                high=score
            print(name+ " your score is "+str(score))    
            input("press enter") #spaces out program a bit, makes them press enter to continue 
            os.system('cls')
            print("***************************************************************************")
            print("Thank you for playing my game" )
            number_of_guesses == 0
            print("your highest score is "+ str(score)) #this is to display the highest score 
            sce =str(high)
            scrLine = str(sce)+"\t "+name + "\t" + date.strftime("%m-%d-%Y")+ "\n"
            myFile = open("number_game.txt",'a') #this opens the file to write 
            myFile.write(scrLine)
            score.sort(reverse=True)
            myFile.close()

