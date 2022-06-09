#Christan Park 
#make user guess a number from 1-25, 1-50, 1-100 
from datetime import date, datetime
from operator import truediv
import os, datetime
import random
import sys
date = datetime.datetime.now()

from pygame import KMOD_SHIFT, K_h
os.system('cls')


def instructions():
    myFile = open("instructions.txt", 'w')
    line1 = "***************************************************************************"
    line2 = " " 
    line3 = "Here are the rules:"
    line4 = "1. Guess a number"
    line5 = "2. You will recieve a hint of higher or lower after each guess"
    line6 = "3. For level 1 you are limited to 5 gueses"
    line7 = "4. For level 2 you are limited to 8 gueses"
    line8 = "5. For level 3 you are limited to 10 gueses"
    line9 = "Have fun and good luck!"
    line10 = " "
    line11 = "***************************************************************************"
    myFile.write(line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5 + "\n" + line6 + "\n" + line7 + "\n" + line8 + "\n" + line9 + "\n" + line10 + "\n" + line11)
    myFile.close()

MENU = True
while MENU:
    print("***************************************************************************") 
    print("") 
    print("Welcome ot Guess a Number!")
    name = input("What is your name? ")
    print("Hi",name)
    print("Choose a selection")
    print("1. Instructions")
    print("2. Guessing from 1-25")
    print("3. Guessing from 1-50")
    print("4. GUessing from 1-100")
    print("5. Print Score")
    print("Exit")
    print("Good Luck " + name + "!")
    print("")
    print("***************************************************************************")
    print("")
    games = True
    while games:
        while True:
            choice = input("What is your selection? ")
            choice=int(choice)
            if choice ==1:
                instructions()
            elif choice == 2:
                print("") 
                print("***************************************************************************") 
                print("") 
                print("Hi",name,", welcome to level 1")
                print("Good Luck!")
                print("")
                print("***************************************************************************")
                print("")

                random_number = random.randint(1,25) #allows computer to choose a number between 1 and 50
                number_of_guesses = 0

                while number_of_guesses < 5: #makes user limited to 5 guesses
                    guess = int(input("Guess a number: ")) #make into int to allow it to be on the same line as a number
                    number_of_guesses += 1
                    if guess < random_number:
                        print('The random number is higher')
                    if guess > random_number:
                        print('The random number is lower')
                    if guess == random_number:
                        break
                if guess == random_number:
                    print("You guessed the number! The number was " + str(random_number) + "!") #make number string to allow to be on the same line as letters
                else:
                    print('Sorry, you ran out of guesses. The number was ' + str(random_number) + ".")

            elif choice == 3:
                print("") 
                print("***************************************************************************") 
                print("") 
                print("Hi",name,", welcome to level 2")
                print("Good Luck!")
                print("")
                print("***************************************************************************")
                print("")

                random_number = random.randint(1,50) #allows computer to choose a number between 1 and 50
                number_of_guesses = 0

                while number_of_guesses < 8: #makes user limited to 8 guesses
                    guess = int(input("Guess a number: ")) #make into int to allow it to be on the same line as a number
                    number_of_guesses += 1
                    if guess < random_number:
                        print('The random number is higher')
                    if guess > random_number:
                        print('The random number is lower')
                    if guess == random_number:
                        break
                if guess == random_number:
                    print("You guessed the number! The number was " + str(random_number) + "!") #make number string to allow to be on the same line as letters
                else:
                    print('Sorry, you ran out of guesses. The number was ' + str(random_number) + ".")

            elif choice == 4:
                print("") 
                print("***************************************************************************") 
                print("") 
                print("Hi",name,", welcome to level 3")
                print("Good Luck!")
                print("")
                print("***************************************************************************")
                print("")

                random_number = random.randint(1,100) #allows computer to choose a number between 1 and 50
                number_of_guesses = 0

                while number_of_guesses < 5: #makes user limited to 5 guesses
                    guess = int(input("Guess a number: ")) #make into int to allow it to be on the same line as a number
                    number_of_guesses += 1
                    if guess < random_number:
                        print('The random number is higher')
                    if guess > random_number:
                        print('The random number is lower')
                    if guess == random_number:
                        break
                if guess == random_number:
                    print("You guessed the number! The number was " + str(random_number) + "!") #make number string to allow to be on the same line as letters
                else:
                    print('Sorry, you ran out of guesses. The number was ' + str(random_number) + ".")
            elif choice ==5:
                score= 2000-40*number_of_guesses 
                print(name+ " your score is "+str(score))    
                input("press enter") #spaces out program a bit, makes them press enter to continue 
                os.system('cls')
                print("***************************************************************************")
                print("Thank you for playing my game" )
                number_of_guesses == 0
                print("your highest score is "+ str(score)) #this is to display the highest score 
                scrLine = str(score)+"\t "+name + "\t" + date.strftime("%m-%d-%Y")+ "\n"
                myFile = open("number_game.txt",'a') #this opens the file to write 
                myFile.write(scrLine)
                myFile.close()
            elif choice ==6:
                print("See you next time!")
                sys.exit()
            else:
                print("Sorry, please choose from 1, 2, 3, 4, 5, or 6!")

