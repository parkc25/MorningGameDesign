#Christan Park 
#We are going to learn about strings '' or ""
#import things
from curses.ascii import isdigit
import os
os.system("cls")
print('Hi')
print("Hi") #no difference between apostraphe
print("Hi, let's go to the park") #use double quotation if use apostraphe in sentence
message="You are awesome" # a string is an array of characters 
# H E L L O 
# 1 2 3 4 5 #all arrays began in zero
print(message) 
print(message[5]) #gets specific number
print(message[0:5]) #prints letters 0-4

if message.isdigit(): #.isdigit is a method you must use with a dot
    sum=message +3 #of statement s true
else:              #if it is false
    print(message+" I say so") #concatenation
print(message.upper())
print(message)
if message.isupper():
    print(message)
else:
    #print("I am in false") #use only for debugging I will selete or comment when done
    message=message.upper()
    print(message)
print(type(message))
print(dir(message)) #tell you everything you can use

