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
print("2. You will have 10 guesses")
print("Good Luck",name,"!")
print("***********************************")
 
list = ['lion','tiger','turtle','penguin','shark','dolphin','whale','bear','wolf']

random_word = random.choice(list)
print('our random word', random_word)






