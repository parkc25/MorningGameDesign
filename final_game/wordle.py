#Christan Park 
# worlde game 

import pygame, sys, os, random
pygame.init()
os.system('cls')

#colors 
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}

#screen/display
colors = ()
WIDTH = 700
HEIGHT = 600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Wordle")
white = (255,255,255)
black = (0,0,0) #change to menu_color later 
green = (0,255,0)
yellow = (255,255,0)
bg_before=pygame.image.load('final_game\images\wordlebackground.jpg')
bg = pygame.transform.scale(bg_before, (700,600))
win_before=pygame.image.load('final_game\images\winning.png')
win = pygame.transform.scale(win_before, (700,600))

#frame rate 
fpr = 60 
timer = pygame.time.Clock()

#board
board = [[" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],]

#fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 55)
win_font = pygame.font.SysFont('comicsans', 45)
again_font = pygame.font.SysFont('comicsans', 20)

#other variables
turn = 0
letters = 0
turn_now = True
game_over = False

#words for game 
# words = ("apple, power,  ")
# random_word = words[random.randint(0, len(words) - 1)]
words = ["power", 'apple','cabin','eager', 'jazzy', 'buzzy', 'fuzzy', 'fizzy','adult', 'anger', 'award', 'beach',
'birth', 'blood', 'brain', 'bread', 'break', 'brown', 'cause', 'chain', 'chair', 'chest', 'child', 'claim', 'class', 'clock'
'cream', 'dance', 'death', 'crown', 'cycle', 'doubt', 'depth', 'draft', 'drama', 'dress', 'dream', 'enemy', 'error', 'entry'
'event', 'faith', 'field', 'flight', 'final', 'floor', 'focus', 'force', 'glass', 'fruit', 'grass', 'green', 'heart', 'group', 
'hotel', 'image', 'index', 'input', 'issue', 'judge', 'knife', 'level', 'light', 'limit', 'lunch', 'major', 'match', 'march', 
'metal', 'model', 'money', 'month', 'music', 'mouth', 'night', 'noise', 'north', 'nurse', 'offer', 'order', 'other', 'owner', 
'panel', 'paper', 'party', 'peace', 'phase', 'phone', 'pilet', 'pitch', 'place', 'plane', 'plant', 'power', 'prize', 'queen', 
'radio', 'replay', 'right', 'round', 'scale', 'scene', 'shape', 'score', 'sheep', 'sense', 'shift', 'shirt', 'skill', 'smoke', 
'speed', 'sport', 'staff', 'stage', 'steam', 'state', 'steel', 'study', 'table', 'sugar', 'taste', 'theme', 'touch', 'tower', 
'track', 'trade', 'train', 'trend', 'trial', 'trust', 'truth', 'uncle', 'union', 'unity', 'video', 'visit', 'voice', 'while', 
'water', 'while', 'world', 'women', 'youth']
random_word = random.choice(words)
print(random_word)

def draw_board(): #making board
    global turn , board
    for col in range (0,5): #0,5 becuase 0 through 4 
        for row in range(0,6): #0,6 becuase 0 through 5 
            pygame.draw.rect(screen, black, [col*100+100, row*100+5, 90, 90], 4,5) # 4, 5 -> making rectangle round and just outline
            letter_font = LETTER_FONT.render(board[row][col], True, black)
            screen.blit(letter_font, (col*100+125, row*100+10))
        pygame.draw.rect(screen, yellow, [5, turn*100, WIDTH-10, 100], 2, 5) #making box around row you are on

def check_word(): #to check if guess = random work
    global turn, board, random_word
    for col in range(0,5):
        for row in range(0,6):
            if random_word[col] == board[row][col] and turn > row: #if a letter in right place making that rect green
                pygame.draw.rect(screen, green, [col*100+100, row*100+5, 90, 90], 0,5)
            elif board[row][col] in random_word and turn > row:
                pygame.draw.rect(screen, yellow, [col*100+100, row*100+5, 90, 90], 0,5) #if letter in word but not right palce making rec yellow

wordle = True 
while wordle:
    timer.tick(fpr) #making game run for 60 frames per minute
    screen.blit(bg,(0,0)) #making background CHANGE LATER
    check_word() #put check word first so the green/yellow box are under what you right
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if press x will take back to menu
            wordle = False
            #mainMenu(title_main, message_menu, True)
        if event.type == pygame.TEXTINPUT and turn_now and not game_over:
            #__getattribute__() is used to retrieve an attribute from an instance
            guess = event.__getattribute__('text') #__getattribute__('text') -> allows user to write with 'text' 
            board[turn][letters] = guess #making guess = new board as letters are added and turn to know when to stop 
            letters += 1 #make it easier for code to add letter so you can put restriction of 5 letters only 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and letters > 0:
                board[turn][letters-1] = ' ' #makes board[turn][letters] back to '' to put new letter
                letters -= 1  #take away letter to allow 5 letters
            if event.key == pygame.K_SPACE: #finalize guess
                turn += 1 #if press space go to next line to make new guess and +turn to make resriction of 5 turns
                letters = 0 #bring letters back to 0 to allow 5 letter guesses
            if event.key == pygame.K_RETURN: #allow game to restart 
                turn = 0 #puts turns back to 0
                letters = 0 #put letter back to zero
                random_word = random.choice(words)
                print(random_word)
                game_over = False 
                # random_word = words[random.randint(0, len(words) -1 )]
                #make board empty to start new game
                board = [[" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],]

    for row in range(0,6):
        guess = board[row][0] + board[row][1] +board[row][2] +board[row][3] +board[row][4] #guess per row and column
        if guess == random_word and row < turn: #allows game to continue untill row>turn 
            game_over = True #ends game

        if letters == 5: #makes turn done if put 5 letters
            turn_now = False
        if letters < 5: #if less than 5 continues game
            turn_now = True

        if turn == 6 and not guess == random_word:
            game_over = True
            screen.fill(white)
            lose_text = LETTER_FONT.render("You lost", True, black)
            screen.blit(lose_text, (WIDTH//2 -100,HEIGHT//2-150))
            word = ("The word was " + random_word)
            word_text = win_font.render( word, True, black)
            screen.blit(word_text, (WIDTH//2 - 200,HEIGHT//2-50))
            playagain_text = again_font.render("To play again press 'enter' and to stop play press the x", 1, black)
            screen.blit(playagain_text, (WIDTH//2 - 250,HEIGHT//6-80))

        if game_over and turn < 7 and guess == random_word: #have to use 'and' and not game_over = True becuase game starts like that if do game wont play 
            screen.blit(win,(0,0))
            win_text = win_font.render("You Win!", True, black)
            screen.blit(win_text, (WIDTH//2 -90,HEIGHT//2-170))
            word = ("The word was " + random_word)
            word_text = win_font.render( word, True, black)
            screen.blit(word_text, (WIDTH//2 - 200,HEIGHT//2+220))
            playagain_text = again_font.render("To play again press 'enter' and to stop play press the x", 1, black)
            screen.blit(playagain_text, (WIDTH//2 - 250,HEIGHT//6-80))

    pygame.display.flip()

    

