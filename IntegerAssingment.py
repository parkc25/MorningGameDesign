#Christan Park 
#Integer Assingment 
import os
os.system("cls")

#Question 1: Is the number even or odd?

num = int(input("Enter any number it test whether it is off or even: "))
if(num % 2 == 0):
    print("The number is even")
else: 
    print("The provided number is off")


#Question 2: Is the number a multiple of 3 or 5?

num = int(input("Enter any number it test whether it is a multiple of 3 or 5: "))
if(num % 3 == 0):
    print("The number is a multiple of 3")
else: 
    print("The number is not a multiple of 3")

if(num % 5 == 0):
    print("The number is a multiple of 5")
else: 
    print("The number is not a multiple of 5")