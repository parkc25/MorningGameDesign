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
number = len(word) #get number of letters in the word
middle2=number//2 #double division ->  integer division
middleFirst = word[middle2-1:middle2+2]
print(middleFirst)
#print("The middle three characters are:",word[middle2-1]+word[middle2]+word[middle2+1])

#Question 3: Append New string in the middle of a given string

word = input('Your word is ') #get word from user
word2 = input('Your second word is ') #get seocnd word 
middleNumber2 = (len(word)//2) #get which number letter is the middle
half1=len(word)//2 #make half1 = middle letter number 
print(word[0:half1]+word2+word[half1:len(word)]) #print first word of word1 to half then insert word2 and rest of word with back half of word1

#Question 4: Create a new string made of the first, middle, and last characters of each input string

word3 = input('Your word is ') #get word from user
word4 = input('Your second word is ') #get second word
first1=word3[0] #get first letter of first word
first2=word4[0] #get  first letter of second word 
middle3=word3[len(word3)//2] #get middle letter of first word
middle4=word4[len(word4)//2] #get middle letter of seocnd word
last2=word3[len(word3)-1] #get last letter of first word
last3=word4[len(word4)-1] #get last letter of second word
print(first1+first2+middle3+middle4+last2+last3) #add all letters together 

#Question 5:Arrange string characters such that lowercase letters should come first

word5 = input('Your word is ')
lower = []
upper = []
for characters in word5:
    if characters.islower(): #islower -> returns True if all characters in the string are lower case
        lower.append(characters) #append moves characters to end of list
    else:
        upper.append(characters) #append moves characters to end of list

print(lower)
print(upper)
sortedWord = ''.join(lower + upper) # join() takes all items and joines them into one string
print('Sorted word is ', sortedWord)

#!!!!! Why need ''. before join???? -> https://stackoverflow.com/questions/14868763/global-name-join-is-not-defined-django


