# Fernando Gupta
# create a word guess agme with 10 words
# pseudocode: provide instructions to user, one hint and the amount of words in the list, get guess. If correct congratulate. if not say you missed. if missed provide another hint. if correct congatulate if inncorect say, man wrong again and then provide third hint, if correct congatulate, if innocorect say you missed again, you are really bad at this, stop providing hits and give user unlimited guesses till correct 

from ctypes.wintypes import WORD
import random
import os, datetime
import sys
date=datetime.datetime.now()

os.system ('cls')
from time import sleep
seconds=.5

theword=""

list1 = ["coral","scallop","sea urchin","oyster","mussel","cockle","clam","geoduck","abelone","ostrea"]
list2 = ["mango", "papaya", "orange","mandarin","clemintine","nectarine","bannana"]
list3 = ["motherboard","CPU","GPU","RAM","SSD","HDD","ROM"]
print()
def selectWrd(choice): #this is a function 
    global theword 
    if choice ==1:
        theword= random.choice(list1) 
        return 
    if choice ==2:
        theword= random.choice(list2)
    if choice ==3:
        theword= random.choice(list3)
Game=True
cnt=0
def hint():
    global cnt  #allows us to modify the variable all over the program 
    if cnt ==0:
        print("that was one guess, you have 4 more")
    elif cnt ==1:
        print("that was another guess, you have 3 more")
    elif cnt ==2:
        print("that was a third guess, you have 2 left")
    elif cnt ==3:
        print("thats 4 guesses, one more ")
    elif cnt ==4:
        print("that 5 guess, last one")
#a function is a section  the prram that we call when we need it

name=input("What is your name? ")
high=0 #to find the highest score 
while Game:
    print("|***************************************|")
    print("|         Guessing  Game   !!           |")
    print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
    print("|          1.animals                    |")
    print("|          2.Fruits                     |")
    print("|      3 Cputer parts                   |")
    print("|           4.QUIT GAME                 |")
    print("|First we will provide you with one hint|")
    print("|           !Your Hint Is!              |")
    print("|  These animals are big fans of water  |")
    print("|***************************************|")
    
# add user name, make it more personal y will need for keeping score
  
    print(name, end=", ")
    answer=input("Would you like to play? ")
    if 'n' in answer:
        break
    while True:
        choice=input("What game would y like to play 1, 2, or 3, or would you quit,4")
        #preventing error we use try and except
        choice=int(choice)
        if choice>0 and choice <4:
                break
        elif choice == 4:
                 sys.exit()
        else:
            print("give me 1,2  3")
            #call function to select the word from the right list

        os.system('cls')


    def hintgiver(choice):
        if choice ==1:
            print("this sea creature almost never moves and has 2 shells")
        if choice ==2:
            print("these fruits are all orange, sweet and popular ")
        if choice ==3:
            print("these components are all importaint to a computer runing well,and are all inside it ")

    check=True
    while check and cnt <5:
        guess=input("plese put your guess here: ")
        print()
        if guess == theword:
            print("Congrats, You got it")
            check=False
        else:
            hint()
        cnt+=1   # cnt= cnt + 1
        if cnt ==5:
            print("sorry!")
    score= 2000-40*cnt 
    if score > high:
        high=score 
    print(name+ " your score is "+str(score))    
    input("press enter") #spaces out program a bit, makes them press enter to continue 
    os.system('cls')
    print("<><><><><><><><><><><><>")
    print("Thank you for playing my game" )
    cnt == 0
print("your highest score is "+ str(high)) #this is to display the highest score 
myFile=open("game.txt",'w') #this opens the file to write 
myFile.write (str(high) + "\t"+name+"\t"+ date.strftime("%m/%d/%Y")) 
myFile.close()