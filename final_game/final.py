#Christan Park
#6/9/2022 - 6/14/2022
#We are learning pygame basic functins, 
# creating screens, clrs, shape ,move 
# move  the square
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
#picture = pygame. image. load(filename)
#picture = pygame. transform. scale(picture, (1280, 720))
#bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')

import sys
import pygame, time,os,random, math
import datetime
from pygame import mixer
from pygame.locals import*
pygame.init()#initialize the pygame package
os.system('cls')

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)

#basic stuff for game
WIDTH=700 #like constant
HEIGHT=600
TITLE_FONT = pygame.font.SysFont('comicsans', 40) #making specific fonts for different text
MENU_FONT = pygame.font.SysFont('comicsans', 20)
score = 0

#clock
clock = pygame.time.Clock()
fps = 60  #frame rate 

#colors for game
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
colors2 = {"grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}

#background colors
menu_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255)) #random color generator

message_menu=['    Wordle Instructions',' Slime Jump Instructions', '             Settings', '              Wordle', '           Slime Jump', '          Scoreboard1','          Scoreboard2' ,'                Exit']
title_main = "Game Menu"

#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #setting screen size to set height and width
pygame.display.set_caption("Christan's Game")  #change the title of my window

#creating buttons
bx = WIDTH//3 #making buttons be in the same spot no matter the size of screen
Button_instruct1 = pygame.Rect(bx, 150, WIDTH//4, 40) #//4 to make words in the center
Button_instruct2 = pygame.Rect(bx, 200, WIDTH//4, 40)
Button_settings = pygame.Rect(bx, 250, WIDTH//4, 40)
Button_game1 = pygame.Rect(bx, 300, WIDTH//4, 40)
Button_game2 = pygame.Rect(bx, 350, WIDTH//4, 40)
Button_score1 = pygame.Rect(bx, 400, WIDTH//4, 40)
Button_score2 = pygame.Rect(bx, 450, WIDTH//4, 40)
Button_exit = pygame.Rect(bx, 500, WIDTH//4, 40)

#images 
bg=pygame.image.load('pygame files\Images\pygame background.jpg')
char = pygame.image.load('pygame files\Images\\alien.jpg')
char = pygame.transform.scale(char, (50, 50))

#wordle images 
bg_before=pygame.image.load('final_game\images\wordlebackground.jpg')
bg = pygame.transform.scale(bg_before, (700,600))
win_before=pygame.image.load('final_game\images\winning.png')
win = pygame.transform.scale(win_before, (700,600))

#background sound
mixer.music.load("pygame files\CircleMenu\\background.wav")
mixer.music.play(0)

#mouse varuables
mx = 0
my = 0

#wordle stuff 
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


def mainMenu(Title, message, MENU):
    global menu_color #have to import undefined variables 
    text_title = TITLE_FONT.render(Title, 1, colors.get("blue")) 
    screen.fill(menu_color)
    xd = WIDTH//2- (text_title.get_width()//2) #to make center by putting width//2 minus the space the words take
    screen.blit(text_title, (xd, 50))
    yMenu=150
    
    for item in message:
        Button_menu=pygame.Rect(bx, yMenu, WIDTH//3, 40)
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        pygame.draw.rect(screen, colors.get('pink'), Button_menu)
        screen.blit(text, (bx, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
    
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #bye-bye screen
                text_title = TITLE_FONT.render("Bye-Bye", 1, colors.get("blue")) 
                screen.fill(menu_color)
                xd = WIDTH//2 - (text_title.get_width()//2) #centering
                yd = HEIGHT//2-40
                screen.blit(text_title, (xd, yd))
                pygame.display.update()
                pygame.time.delay(2000) #show bye-bye screen for 2 seconds
                pygame.quit()
                sys.exit()

            #making collidepoints
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_instruct1.collidepoint((mx, my)):
                    content = readFile("Wordle Instructions", "final_game\instructions1.txt")
                if Button_instruct2.collidepoint((mx, my)):
                    readFile("Slime Jump Instructions", "final_game\instructions2.txt")
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_game1.collidepoint((mx, my)):
                    Game_1()
                if Button_game2.collidepoint((mx, my)):
                    Game_2()
                if Button_score1.collidepoint((mx, my)):
                    readFile("Wordle Scoreboard", "final_game\wordleScore.txt")
                if Button_score2.collidepoint((mx, my)):
                    readFile("Slime Jump Scoreboard", "final_game\slimpJumpScore.txt")
                if Button_exit.collidepoint((mx, my)):
                    exit()

def settings():
    global menu_color, screen, WIDTH, HEIGHT
    screen.fill(menu_color)
    #getting text for button 
    Title2=TITLE_FONT.render('Settings', 1, colors.get('blue'))
    text2=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
    text3=MENU_FONT.render('On', 1, colors.get('blue'))
    text4=MENU_FONT.render('Off', 1, colors.get('blue'))
    text5=MENU_FONT.render('Random', 1, colors.get('blue'))
    text6=MENU_FONT.render('Original Size', 1, colors.get('blue'))
    text7=MENU_FONT.render('Width +100', 1, colors.get('blue'))
    text8=MENU_FONT.render('Width-100', 1, colors.get('blue'))

    myFile = open("final_game\settings.txt", "r") #bring in settings file
    content = myFile.readlines()
    myFile.close()

    yi = 100
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yi))
        pygame.display.update()
        # pygame.time.delay(50)
        yi += 40

    #making buttons for game
    Button_2 = pygame.Rect(450, HEIGHT//6+400, 200, 50)
    Button_color = pygame.Rect(WIDTH//2-100, HEIGHT//6+60, 200, 50)
    Button_sound_on = pygame.Rect(WIDTH//4, HEIGHT//6+160, 150, 50)
    Button_sound_off = pygame.Rect(WIDTH//4+200, HEIGHT//6+160, 150, 50)
    Button_size0 = pygame.Rect(WIDTH//7, HEIGHT//6+290, 150, 50)
    Button_size1 = pygame.Rect(WIDTH//7+175, HEIGHT//6+290, 150, 50)
    Button_size2 = pygame.Rect(WIDTH//7+350, HEIGHT//6+290, 150, 50)

    #making colors for button
    pygame.draw.rect(screen, colors.get("pink"), Button_2)
    pygame.draw.rect(screen, colors.get("pink"), Button_color)
    pygame.draw.rect(screen, colors.get("pink"), Button_sound_on)
    pygame.draw.rect(screen, colors.get("pink"), Button_sound_off)
    pygame.draw.rect(screen, colors.get("pink"), Button_size0)
    pygame.draw.rect(screen, colors.get("pink"), Button_size1)
    pygame.draw.rect(screen, colors.get("pink"), Button_size2)

    #placement of words on screen
    xd = WIDTH//2 - (Title2.get_width()//2)
    a = WIDTH//4 
    b = WIDTH//2
    c = WIDTH//7
    screen.blit(Title2, (xd, 50))
    screen.blit(text2, (480,HEIGHT//6+405))
    screen.blit(text3, (a+55,265))
    screen.blit(text4, (a+255,265))
    screen.blit(text5, (b-40,165))
    screen.blit(text6, (c+20,400))
    screen.blit(text7, (c+195,400))
    screen.blit(text8, (c+375,400))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #if press x go back to menu
                run=False
                mainMenu(title_main, message_menu, True)
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_2.collidepoint((mx, my)): #return button take back to menu
                    mainMenu(title_main, message_menu, True)
                if Button_sound_on.collidepoint((mx,my)):
                    mixer.music.play(-1)
                    print("music on")
                if Button_sound_off.collidepoint((mx,my)):
                    mixer.music.stop()
                    print("music off")
                if Button_size0.collidepoint((mx,my)):
                    screen=pygame.display.set_mode((700,600)) 
                if Button_size1.collidepoint((mx,my)):
                    WIDTH+=100
                    screen=pygame.display.set_mode((WIDTH,HEIGHT))
                    pygame.display.update()
                if Button_size2.collidepoint((mx, my)) and WIDTH > 600: 
                    WIDTH-=100
                    screen=pygame.display.set_mode((WIDTH,HEIGHT))
                    pygame.display.update() 
                if Button_color.collidepoint((mx,my)): #change background color
                    menu_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255)) #MUST BE = not ==
                    print("change color")
                pygame.display.update()
                settings()
            
def readFile(titleF, fileN):
    global menu_color
    #fill screen with white
    screen.fill(menu_color)
    #rendering text objects
    Title=TITLE_FONT.render(titleF, 1, colors.get('blue'))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd,50))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("blue"))

    #making button
    Button_3 = pygame.Rect(480, HEIGHT//6+420, 200, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_3)


    #Instructions
    myFile = open(fileN, "r")
    content = myFile.readlines()
    myFile.close()

    #var to controll change of line
    yinstructions = 110
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()
    
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    screen.blit(text3, (510,HEIGHT//6+430))
    pygame.display.update()

    scoreboard=True
    while scoreboard:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                mainMenu(title_main, message_menu, True)
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu(title_main, message_menu, True)

    high=0
    title=TITLE_FONT.render('Scoreboard', 1, colors.get('blue'))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("blue"))

    screen.fill(menu_color)
    Button_3 = pygame.Rect(450, 600, 200, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_3)
    
    screen.blit(title, (WIDTH//3,50))
    screen.blit(text3, (480,605))
    pygame.display.update()

def Game_1(): #ADD SCOREEEEE
    def draw_board(): #making board
        global turn , board
        for col in range (0,5): #0,5 becuase 0 through 4 
            for row in range(0,6): #0,6 becuase 0 through 5 
                pygame.draw.rect(screen, colors2.get("black"), [col*100+100, row*100+5, 90, 90], 4,5) # 4, 5 -> making rectangle round and just outline
                letter_font = LETTER_FONT.render(board[row][col], True, colors2.get("black"))
                screen.blit(letter_font, (col*100+125, row*100+10))
            pygame.draw.rect(screen, colors2.get("yellow"), [5, turn*100, WIDTH-10, 100], 2, 5) #making box around row you are on

    def check_word(): #to check if guess = random work
        global turn, board, random_word
        for col in range(0,5):
            for row in range(0,6):
                if random_word[col] == board[row][col] and turn > row: #if a letter in right place making that rect green
                    pygame.draw.rect(screen, colors2.get("green"), [col*100+100, row*100+5, 90, 90], 0,5)
                elif board[row][col] in random_word and turn > row:
                    pygame.draw.rect(screen, colors2.get("yellow"), [col*100+100, row*100+5, 90, 90], 0,5) #if letter in word but not right palce making rec yellow

    wordle = True 
    while wordle:
        clock.tick(fps) #making game run for 60 frames per minute
        screen.blit(bg,(0,0)) #making background CHANGE LATER
        check_word() #put check word first so the green/yellow box are under what you right
        draw_board()
        global board, random_word, turn, letters, turn_now, game_over

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if press x will take back to menu
                mainMenu(title_main, message_menu, True)
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

            if turn == 6 and not guess == random_word: #if guess 5 words and didnt get it show this
                game_over = True #game is over
                screen.fill(colors.get("white")) #white background
                lose_text = LETTER_FONT.render("You lost", True, colors2.get("black")) #printing they lost
                screen.blit(lose_text, (WIDTH//2 -100,HEIGHT//2-150)) #placement of lose text
                word = ("The word was " + random_word) #telling what word it was
                word_text = win_font.render( word, True, colors2.get("black")) #setting color and font of telling what word
                screen.blit(word_text, (WIDTH//2 - 200,HEIGHT//2-50)) #placement of what word text
                playagain_text = again_font.render("To play again press 'enter' and to stop playing press the x", 1, colors2.get("black")) #telling them how to play again or exit
                screen.blit(playagain_text, (WIDTH//2 - 245,HEIGHT//6-80)) #placement of play again or not text 

            if game_over and turn < 7 and guess == random_word: #have to use 'and' and not game_over = True becuase game starts like that if do game wont play 
                screen.blit(win,(0,0)) #setting trophy background
                win_text = win_font.render("You Win!", True, colors2.get("black")) #printing they won and setting color and font
                screen.blit(win_text, (WIDTH//2 -90,HEIGHT//2-170)) #placement of winning text 
                word = ("The word was " + random_word) #printing what word was in case they forgot
                word_text = win_font.render( word, True, colors2.get("black")) #setting color and font
                screen.blit(word_text, (WIDTH//2 - 200,HEIGHT//2+220)) #setting placement of word text 
                playagain_text = again_font.render("To play again press 'enter' and to stop playing press the x", 1, colors2.get("black")) #telling them how to play again or exit
                screen.blit(playagain_text, (WIDTH//2 - 245,HEIGHT//6-80)) #placement of play again or not text 

        pygame.display.flip() #llows only a portion of the screen to updated, instead of the entire area -> this case just game 

def Game_2():
   Slime_Jump = True 
   while Slime_Jump:
        clock.tick(fps)
        black = colors2.get("black")
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainMenu(title_main, message_menu, True)
            
def name():
    screen.fill(menu_color)
    run = True 
    user_name = ''
    nameClr = (0,105,105)
    bxClr = (200,200,200)

    title = TITLE_FONT.render("Enter name ", 1, bxClr)
    screen.blit(title, (WIDTH//2-100,200))
    pygame.time.delay(500)

    pygame.display.update()

    name_box = pygame.Rect(WIDTH/2-90, HEIGHT//2, 200, 50)
    while run:
        for event in pygame.event.get():
                if event.type==pygame.QUIT: #if press x go back to menu
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    #make box 
                    name_box = pygame.Rect(WIDTH/2-90, HEIGHT//2, 200, 50)
                    pygame.draw.rect(screen, colors.get("white"), name_box)
                    pygame.display.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        mainMenu(title_main, message_menu, True)
                    if event == pygame.K_BACKSPACE:
                        user_name = user_name[:-1]
                    else:
                        user_name+= event.unicode
                pygame.draw.rect(screen, bxClr, name_box)

                text_surface = MENU_FONT.render(user_name, True, nameClr)
                #user ur rect x, y, to 
                screen.blit(text_surface, (name_box.x+5, name_box.y+5))

                pygame.display.flip()

                #clock.tick(60) means that for every second at most  60 frams should be passed
                clock.tick(60)

def exit():
    title=TITLE_FONT.render('Bye-Bye', 1, colors.get('blue'))
    screen.fill(menu_color)
    screen.blit(title, (275,200))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit() 

name()
mainMenu(title_main, message_menu, True)