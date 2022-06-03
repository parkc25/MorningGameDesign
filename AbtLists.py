#Christan Park 
#We are going to learn about lists, functions to list
#We are also going to learn about for loop
import os
from random import random
os.system('cls')

list = ['apple','banana','cherry','orange','kiwi','melon','mango']
#           1       2       3         4       5      6       7
print(list[1]) #get first element (ie banana)
print(list[-1]) #get last element
print(list[2:5]) #gets elements 2-4 (excludes last element)
print(list[:3]) #gets 0-2 (excluding element 3)
print(list[2:]) #gets 2-end (includes last one)
print(list[-4:-1]) #gets 4-6 (excludes 7)

fruit = input("What fruits do we have? ")
if fruit in list:
    print("Yes, we have", fruit)
else:
    print("No, we do not have", fruit)

#for num in range(10):
    #print(num, end = "")

print() #adds space to make new line from one element to the next/use with end='

for element in list: #element = list[times run through the loop]
    print(element, end = ' ')

print()

list.append("pineapple") #adds pineapple to end of list
print(list[0:])

for num in range(10): #ask user 10 different fruits/elements
    list.append(input("Name a fruit "))
print(list[0:])

list.insert(0,"pineapple")
print(list[0:])

for i in range(len(list)):
    print(i, end = ' ')
print()

list_num = [1,2,3,4]
list_num.extend(list) #everything in the list + list_num (added to front)
print(list_num)
list_num.append(list) #adds list to end of list (list in a list)
print(list_num)

word = random.choice(list)
print(word)

guess = input("Guess a fruit")
if guess in word:
    print("Congrats you guessed the fruit")
else:
    print("Sorry, try again :(")


