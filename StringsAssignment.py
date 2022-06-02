#Christan Park
#worksheet on strings 
import os
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
number = (len(word)) #get the number of letters in the word
middleNumber2 = int(number/2) #get the number of the middle digit in word
middle2 = word[middleNumber2] #get the middle letter
firstmiddle = middle2 - 1
lastmiddle = middle2 + 1
print(firstmiddle + middle2 + lastmiddle)








