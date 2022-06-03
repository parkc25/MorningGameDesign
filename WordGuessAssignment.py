#Christan Park 
#Make a list of at least 10 words
#Randomly select a word
#ask the user to guess the word (give a hint about what kind of words you are using: fruits, animals,etc)
#If they guess right congratulate them if mot say sorry "you missed"
import os
import random
os.system('cls')

print("***********************************")
print("Welcome to Guess The Animal!")
name = input("What is your name? ")
print("Hi",name,", here are the rules:")
print("1. Guess a animal")
print("2. You can guess until you win!")
print("Good Luck",name,"!")
print("***********************************")
 
list = ['lion','tiger','turtle','penguin','shark','dolphin','whale','bear','wolf']

random_word = random.choice(list)
guess = ''

print("")
while guess != random_word:
    guess = input("Guess an animal: ")
    print("Sorry that is incorrect, try again!")

print("You win! The coreect word was", random_word)
print("***********************************")








