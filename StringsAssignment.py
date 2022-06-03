#Christan Park
#worksheet on strings 
import os
from re import X
from tkinter import Y
os.system("cls")

#Question 1: get first middle and last letters

#method 1
a = "James"
print(len(a)) #number of letter in word
print(a[0], end='') #get first letter
print(a[2], end='') #put middle letter on same line
print(a[4]) #put last letter on same line

#method 2
word = input('Your word is ') #get word from user
number = (len(word)) #get the number of letters in the word
first = word[0] #get first letter of word
middleNumber = int(number/2) #get the number of the middle digit in word
middle = word[middleNumber] #get the middle letter
last = word[number-1] #get last letter
print(first+middle+last) #print first middle and last letter together 


#Question 2: Create a string made of the middle three characters

word = input('Your word is ') #get word from user
number = len(word) #get number of letters in the word
middle2=number//2 #double division ->  integer division
middleFirst = word[middle2-1:middle2+2]
print(middleFirst)
#print("The middle three characters are:",word[middle2-1]+word[middle2]+word[middle2+1])

#Question 3: Append New string in the middle of a given string

word = input('Your word is ') #get word from user
word2 = input('Your second word is ')
middleNumber2 = (len(word)//2)
half1=len(word)//2
print(word[0:half1]+word2+word[half1:len(word)])

#Question 4: Create a new string made of the first, middle, and last characters of each input string

word3 = input('Your word is ') #get word from user
word4 = input('Your second word is ')
first1=word3[0]
first2=word4[0]
middle3=word3[len(word3)//2]
middle4=word4[len(word4)//2]
last2=word3[len(word3)-1]
last3=word4[len(word4)-1]
print(first1+first2+middle3+middle4+last2+last3)

#Question 5:Arrange string characters such that lowercase letters should come first

word5 = input('Your word is ')
word5.sort



















