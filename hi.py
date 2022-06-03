#Christan Park 
#We are going to learn about lists, functions to list
#We are also going to learn about for loop
import os
from random import random
os.system('cls')

list = ['apple','banana','cherry','orange','kiwi','melon','mango']

word = random.choice(list)
print(word)

guess = input("Guess a fruit")
if guess in word:
    print("Congrats you guessed the fruit")
else:
    print("Sorry, try again :(")