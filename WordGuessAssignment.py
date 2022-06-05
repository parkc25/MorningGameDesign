#Christan Park 
#Make a list of at least 10 words
#Randomly select a word
#ask the user to guess the word (give a hint about what kind of words you are using: fruits, animals,etc)
#If they guess right congratulate them if mot say sorry "you missed"
from operator import truediv
import os
import random

from pygame import K_h
os.system('cls')

#Game with Unlimited Guesses 

#
print("***************************************************************************") 
print("") 
print("Welcome to Guess The Number!")
name = input("What is your name? ")
print("Hi",name,", here are the rules:")
print("1. Guess a number from 0 to 50")
print("2. You have 5 guesses")
print("3. After each incorrect guess you will recieve a hint of lower or higher")
print("3. Guess till you win!")
print("Good Luck",name,"!")
print("")
print("***************************************************************************")
print("")

random_number = random.randint(1,50)
number_of_guesses = 0
#print("The random number is", random_number)

while number_of_guesses < 5:
    guess = int(input("Guess a number: "))
    number_of_guesses += 1
    if guess < random_number:
        print('The random number is higher')
    if guess > random_number:
        print('The random number is lower')
    if guess == random_number:
        break
print("")
if guess == random_number:
    print("You guessed the number! The number was " + str(random_number) + "!")
else:
    print('Sorry, you did not guess the number. The number was ' + str(random_number) + ".")
print("")
print("***************************************************************************")
print("")
print("Thank you for playing! If you want to play again type 'yes' or 'no' below!")
play_again = input("Do you want to play again? ")
if input == "yes": 
    p
else:
    print("Ok, see you later and thank you for playing!")
print("")
print("***************************************************************************")

