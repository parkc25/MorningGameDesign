#Christan Park 
#We are going to learn about lists, functions to list
#We are also going to learn about for loop
import os
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

for num in range(10):
    print(num, end = "")

print() #adds space to make new line from one element to the next/use with end='

for element in list: #element = list[times run through the loop]
    print(element, end = ' ')

print()

list.append("pineapple")
print(list[0:])

