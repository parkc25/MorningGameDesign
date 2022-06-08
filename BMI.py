#Christan Park 
#import things
import os
os.system("cls")
height=int(input('height in inches ')) #use int to make string of number into integer
weight=int(input('weight in pounds ')) #use int to make string of number into integer
BMI=weight/(height*height)*703 #equation for BMI
print('Your BMI is',BMI) #tell them their BMI
#use these comparisons to find if they are underwieght, normal, or obese
if BMI<=18.5: #<= -> less than or equal to 
    print("You are underweight")
elif BMI<=25:
    print("You are normal")
elif BMI<=30:
    print("You are obese")
else:
    print("You are obese")