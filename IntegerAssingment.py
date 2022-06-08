#Christan Park 
#Integer Assingment 
import os
os.system("cls")

#Question 1: Is the number even or odd?

num = int(input("Enter any number it test whether it is off or even: ")) #ask user to put in number
if(num % 2 == 0): #equation ask if when number is divided by 2 it equals zero. If so, it is even if not odd.
    print("The number is even")
else: 
    print("The provided number is off")


#Question 2: Is the number a multiple of 3 and 5?

num = int(input("Enter any number it test whether it is a multiple of 3 and 5: ")) #ask user to put in number
if(num % 3 == 0 and num % 5 == 0): #test if when number is divided by 3 and 5 it is equal to zero. If so, it can be divided. 
    print("The number is a multiple of 3 and 5")
else:
    print("The number is not a multiple of 3 and 5")
