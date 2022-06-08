#Christan Park 
#Make a list of at least 10 words
#Randomly select a word
#ask the user to guess the word (give a hint about what kind of words you are using: fruits, animals,etc)
#If they guess right congratulate them if mot say sorry "you missed"
from ctypes.wintypes import WORD
import os
import random
os.system('cls')
from time import sleep 
seconds=.5

#Game with Unlimited Guesses 
#make game pretty, tell them what it is about, and how to play

the_word = ""
list1 = ['cherry', 'strawberry', 'red apple', 'raspberry', 'cherry', 'plum', 'red cactus fruit', 'red passion fruit', 'red dragon fruit', 'lychee', 'red grapes']
list2 = ['ethiopian wolf', 'black rhino', 'white rhino', 'mountain gorilla', 'african wild dog', "rothschild's giraffe", 'chimpanzee', "cuvier's atlas gazelle", 'cheetahs', 'pygmy hippo']
list3 = random.randint(1,50)

game = True 
cnt = 0 
def hint():
    global cnt 
    if cnt == 0:
        print("Here is the first hint:")
        print("This food is a fruit ")
    elif cnt == 1: 
        print("Here is the second hint:")
        print("This fruit is red ")
    else: 
        print("Sorry, you have run out of hints. Good Luck!")
    print()

def hint2():
    global cnt
    if cnt == 0:
        print("Here is the first hint:")
        print("This animal lives in Africa")
    if cnt == 1:
        print("Here is the second hint:")
        print("This animal is a mammal")
    if cnt == 2:
        print("Here is the last hint:")
        print("This animal is endangered")

def selectWrd(choice):
    global the_word
    if choice ==1:
        the_word = random.choice(list1)
    if choice ==2:
        the_word = random.choice(list2)
    if choice ==3:
        the_word = list3

while game:
    print("***************************************************************************") 
    print("") 
    print("Welcome!")
    name = input("What is your name? ")
    print("Hi",name,", here are the rules:")
    print("Pick a game below and play it!")
    print("1. Guess the Number")
    print("2. Guess the Food")
    print("3. Guess the Animal")
    print("Good Luck " + name + "!")
    print("")
    print("***************************************************************************")
    print("")
    answer = input("Would you like to play? ")
    if "no" in answer:
        break
    while True:
        choice = input("What game do you want to play? 1, 2, or 3? ")
        try:
            choice=int(choice)
            if choice>0 and choice<4:
                break
            else:
                print("Sorry we don't have that game please choose from 1, 2, or 3!")
        except:
            print("Sorry we don't have that game please choose from 1, 2, or 3!")
    the_word = selectWrd(choice)
    os.system('cls')
    check = True
    while check and cnt <5:
        guess = input("Your guess: ")
        print("")
        if guess == the_word:
            print("That is the correct!")
            check = False
        else: 
            hint()
        cent=+1
        if cnt ==5:
            print("Sorry!")
            
    
    score = 200-40*cnt
    if score > high:
        high = score
    print(name + ", your score is " + str(score))
    input("Press enter")
    os.system('cls')
    print("***************************************************")
    answer = input("Do you want to play again? ")
    if ('no' or 'No') in answer:
        game = False
        print("Thank you for playing my game!")





        if choice == 1:
            number_game = True
            while number_game:
                print("***************************************************************************") 
                print("") 
                print("Welcome to Guess The Number!")
                print("Hi",name,", here are the rules:")
                print("1. Guess a number from 0 to 50")
                print("2. You have 5 guesses")
                print("3. After each incorrect guess you will recieve a hint of lower or higher")
                print("Good Luck",name,"!")
                print("")
                print("***************************************************************************")
                print("")

                random_number = random.randint(1,50) #allows computer to choose a number between 1 and 50
                number_of_guesses = 0
                #print("The random number is", random_number)

                while number_of_guesses < 5: #makes user limited to 5 guesses
                    guess = int(input("Guess a number: ")) #make into int to allow it to be on the same line as a number
                    number_of_guesses += 1
                    if guess < random_number:
                        print('The random number is higher')
                    if guess > random_number:
                        print('The random number is lower')
                    if guess == random_number:
                        break
                print("")
                if guess == random_number:
                    print("You guessed the number! The number was " + str(random_number) + "!") #make number string to allow to be on the same line as letters
                else:
                    print('Sorry, you did not guess the number. The number was ' + str(random_number) + ".")
                print("")
                print("***************************************************************************")
                print("")
                print("Thank you for playing! You guessed it in "+ str(number_of_guesses) + " tries!")
                print("Would you like to play the number game again, choose a new game. or not play at all? ")
                print("To play the number game again type '1'")
                print("To play another game type '2'")
                print("To stop playing type '3'")
                play_again = int(input("Type your response here: "))
                if play_again == 1: 
                    number_game=True
                    print("")
                elif play_again == 2: 
                    all_games=True 
                    print("")
                elif play_again == 3:
                    print("Ok, see you later and thank you for playing!")
                    all_games = False
                    number_game = False
                    print("")
                    print("***************************************************************************")
                else:
                    print("Ok, see you later and thank you for playing!")
                    all_games = False
                    number_game = False
                    print("")
                    print("***************************************************************************")
        elif choice == 2:
            food_game = True
            while food_game:
                print("***************************************************************************") 
                print("") 
                print("Welcome to Guess The Food!")
                print("Hi",name,", here are the rules:")
                print("1. Guess a food")
                print("2. You have 4 guesses")
                print("3. After each incorrect guess you will recieve a hint of the food")
                print("Good Luck",name,"!")
                print("")
                print("***************************************************************************")
                print("")

                list_of_food = ['cherry', 'strawberry', 'red apple', 'raspberry', 'cherry', 'plum', 'red cactus fruit', 'red passion fruit', 'red dragon fruit', 'lychee', 'red grapes']
                random_food = random.choice(list_of_food)
                number_of_guesses = 0 
                print(random_food)

                while number_of_guesses < 3: #makes user limited to 5 guesses
                    guess = input("Guess a food: ") #make into int to allow it to be on the same line as a number
                    if guess == random_food:
                        print("That is correct! The food was " + random_food + "!")
                        break
                    else:
                        print("Sorry that is inorrect")
                    print("")
                    print("Here is the first hint:")
                    print("This food is a either a fruit or vegatable")
                    guess2 = input("Guess a fruit or vegatable: ")
                    if guess2 == random_food:
                        print("That is correct! The food was " + random_food + "!")
                        break
                    else: 
                        print("Sorry that is inorrect")
                    print("")
                    print("Here is the second hint:")
                    print("This food is a fruit not a vegatable")
                    guess3 = input("Guess a fruit: ")
                    if guess3 == random_food:
                        print("That is correct! The food was " + random_food + "!")
                        break
                    else: 
                        print("Sorry that is inorrect")
                    print("")
                    print("Here is the last hint:")
                    print("This fruit is red")
                    guess4 = input("Guess a red fruit: ")
                    if guess4 == random_food:
                        print("That is correct! The food was " + random_food + "!")
                        break
                    else: 
                        print("Sorry that is inorrect. The food was " + random_food + "!")
                        break
                print("")
                print("***************************************************************************")
                print("")
                print("Thank you for playing! You guessed it in "+ str(number_of_guesses) + " tries!")
                print("Would you like to play the number game again, choose a new game. or not play at all? ")
                print("To play the food game again type '1'")
                print("To play another game type '2'")
                print("To stop playing type '3'")
                play_again = int(input("Type your response here: "))
                if play_again == 1: 
                    food_game=True
                    print("")
                elif play_again == 2: 
                    start_game=True 
                    print("")
                elif play_again == 3:
                    print("Ok, see you later and thank you for playing!")
                    all_games = False
                    food_game = False
                    print("")
                    print("***************************************************************************")
                else:
                    print("Ok, see you later and thank you for playing!")
                    all_games = False
                    food_game = False
                    print("")
                    print("***************************************************************************")
        elif choice == 3:
            animal_game = True
            while animal_game:
                print("***************************************************************************") 
                print("") 
                print("Welcome to Guess The Animal!")
                print("Hi",name,", here are the rules:")
                print("1. Guess an animal")
                print("2. You have 4 guesses")
                print("3. After each incorrect guess you will recieve a hint of the animal")
                print("Good Luck",name,"!")
                print("")
                print("***************************************************************************")
                print("")

                list_of_animals = ['ethiopian wolf', 'black rhino', 'white rhino', 'mountain gorilla', 'african wild dog', "rothschild's giraffe", 'chimpanzee', "cuvier's atlas gazelle", 'cheetahs', 'pygmy hippo']
                random_animal = random.choice(list_of_animals)
                number_of_guesses = 0 
                print(random_animal)

                while number_of_guesses < 3: #makes user limited to 5 guesses
                    guess = input("Guess a food: ") #make into int to allow it to be on the same line as a number
                    if guess == random_animal:
                        print("That is correct! The food was " + random_animal + "!")
                        break
                    else:
                        print("Sorry that is inorrect")
                    print("")
                    print("Here is the first hint:")
                    print("This animal lives in Africa")
                    guess2 = input("Guess an animal: ")
                    if guess2 == random_animal:
                        print("That is correct! The food was " + random_animal + "!")
                        break
                    else: 
                        print("Sorry that is inorrect")
                    print("")
                    print("Here is the second hint:")
                    print("This animal is a mammal")
                    guess3 = input("Guess an animal: ")
                    if guess3 == random_animal:
                        print("That is correct! The food was " + random_animal + "!")
                        break
                    else: 
                        print("Sorry that is inorrect")
                    print("")
                    print("Here is the last hint:")
                    print("This animal is endangered")
                    guess4 = input("Guess an animal: ")
                    if guess4 == random_animal:
                        print("That is correct! The animal was " + random_animal + "!")
                        break
                    else: 
                        print("Sorry that is inorrect. The food was " + random_animal + "!")
                        break
                print("")
                print("***************************************************************************")
                print("")
                print("Thank you for playing! You guessed it in "+ str(number_of_guesses) + " tries!")
                print("Would you like to play the number game again, choose a new game. or not play at all? ")
                print("To play the animal game again type '1'")
                print("To play another game type '2'")
                print("To stop playing type '3'")
                play_again = int(input("Type your response here: "))
                if play_again == 1: 
                    food_game=True
                    print("")
                elif play_again == 2: 
                    start_game=True 
                    print("")
                elif play_again == 3:
                    print("Ok, see you later and thank you for playing!")
                    all_games = False
                    food_game = False
                    print("")
                    print("***************************************************************************")
                else:
                    print("Ok, see you later and thank you for playing!")
                    all_games = False
                    food_game = False
                    print("")
                    print("***************************************************************************")
        else:
            print("Sorry we don't have that game please choose from 1, 2, or 3!")
            