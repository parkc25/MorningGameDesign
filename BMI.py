#Christan Park 
#import things
import os
os.system("cls")
#put height in inches 
height=int(input('height in inches '))
weight=int(input('weight in pounds '))
BMI=weight/(height*height)*703
if BMI<18.5:
    print("You are underweight")
if BMI<20:
    print("You are normal")
if BMI<30:
    print("You are obese")
else:
    print("You are obese")