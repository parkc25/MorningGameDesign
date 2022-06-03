#Christan Park 
#Make a list of at least 10 words
#Randomly select a word
#ask the user to guess the word (give a hint about what kind of words you are using: fruits, animals,etc)
#If they guess right congratulate them if mot say sorry "you missed"
import os
import random
os.system('cls')

#Game with Unlimited Guesses 

print("****************************************")
print("Welcome to Guess The Animal!")
name = input("What is your name? ")
print("Hi",name,", here are the rules:")
print("1. Guess a animal")
print("2. You have unlimited guesses")
print("3. Guess till you win!")
print("Good Luck",name,"!")
print("****************************************")
 
list = ['lion','tiger','turtle','penguin','shark','dolphin','whale','bear','wolf']

random_word = random.choice(list)
print("The random word is", random_word)
guess = ''

print("")
while guess != random_word:
    guess = input("Guess an animal: ")
    if guess != random_word:
        print("Sorry that is incorrect, try again!")
    if guess == random_word:
        print("You win! The coreect word was", random_word)
print("")
print("Do you want to play again?")
play_again = input("Type Y if yes or N if no ")
if play_again == "N":
    
print("****************************************")






