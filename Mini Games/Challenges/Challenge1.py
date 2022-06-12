#Christan Park 
#first let's import random procedures since we will be shuffling
import random, os
os.system('cls')
deck=[]
#next, let's start building list holders so we can place our cards in there:
def create_DECK():
    global deck
    numberCards = []
    suits = ["♥️","♦️", "♣️", "♠️"]
    royals = ["J", "Q", "K", "A"]

    #now, let's start using loops to add our content:
    for i in range(2,11):
        numberCards.append(str(i))
        #this adds numbers 2-10 and converts them to string data

    for j in range(4):
        numberCards.append(royals[j])
        #this will add the royal faces to the cardbase
    
    for k in range(4):
        for l in range(13):
            card = (numberCards[l] + " " + suits[k])
            #this makes each card, cycling through suits, but first through faces
            deck.append(card)
            #this adds the information to the "full deck" we want to make
    #now let's see the cards!
    counter=0
    for row in range(4):
        for col in range(13):
            print(deck[counter], end=" ")
            counter +=1
        print()
    #deck before shuffling
    print(deck)
    print("")
create_DECK()

#now let's shuffle our deck!
def playerCards():
    random.shuffle(deck)
    player1_deck=[]
    player2_deck=[]
    for l in range(52):
        if l%2==0:
            player1_deck.append(deck[l])
        else:
            player2_deck.append(deck[l])
    print("player1 ",player1_deck)
    print()
    print("player2 ",player2_deck)
    #I also want to see what the deck looks like before shuffling. We should have
        #done that a while ago... oh well!
playerCards()
print("")

def draw_card(player):
    card = deck[0]
    deck.remove(deck[0])
    print(player + ' drew the ' + str(card))
    return card    

def compare_scores(card1, card2):
    if card1 == card2:
        return 0
    if card1 > card2:
        return 1
    else:
        return 2


player1 = input("Please enter player 1's name: ")
player2 = input("Please enter player 2's name: ")
player1_score = 0
player2_score = 0
player1_deck = []
player2_deck = []

#Game part
while True:
    #each player draws a card
    player1_card = draw_card(player1)
    player2_card = draw_card(player2)
    #compare cards 
    if player1_card[0] > player2_card[0]:
        winner = player1
        player1_score += 2
    elif player1_card[0] < player2_card[0]:
        winner = player2
        player2_score += 2
    else:
        winner = "Tie, draw again!"
    print(winner + ' wins!')      

    #if tie
    print("War!!!")
    war_pool = [player1_card, player2_card]
    while compare_cards ==0:
        player1_card = player_turn(player1, playerCards)
        player2_card = player_turn(player2, playerCards)

        war_pool.append(player1_card)
        war_pool.append(player2_card)
        compare_cards = compare_scores(player1_card, player2_card)

        if compare_cards ==1:
            print(player1 + "has the higher card!")
            player1_deck.extend(war_pool)
            player1_score = len(player1_deck)
            print(player1 + ": " +str(player1_score) +" vs. " + player2 + ": " + str(player2_score))
            print("")
        elif compare_cards ==2:
            print(player2 + "has the higher card!")
            player2_deck.extend(war_pool)
            player2_score = len(player2_deck)
            print(player1 + ": " +str(player1_score) +" vs. " + player2 + ": " + str(player2_score))
            print("")


    #check if deck is empty 
    if len(deck) == 0:
        print("Game over. " + winner + " wins the game!")
        print("Player 1 had " + str(player1_score) +" points")
        print("Player 2 had " + str(player2_score) +" points")

