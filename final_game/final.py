#Christan Park
#6/20/2022 = 6/24/2022 
#Final Project - Wordle and Slime Jump 

import sys
from tkinter import E
import pygame,os,random
import datetime
from pygame import mixer
from pygame.locals import*
pygame.init()#initialize the pygame package
os.system('cls') #clear terminal

#basic stuff for game
WIDTH=700 
HEIGHT=600
TITLE_FONT = pygame.font.SysFont('comicsans', 40) #making specific fonts for different text
MENU_FONT = pygame.font.SysFont('comicsans', 20)

#clock
clock = pygame.time.Clock()
fpr = 60  #frame rate 

#background sound
mixer.music.load("pygame files\CircleMenu\\background.wav")
mixer.music.play(0)
# mixer.music.stop()

#mouse varuables
mx = 0
my = 0

#colors for game
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
colors2 = {"grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}

#background color
menu_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255)) #random color generator

#Screen Name and Size
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #setting screen size to set height and width
pygame.display.set_caption("Christan's Game")  #change the title of my window

#Names of Buttons on Main Menu
message_menu=['    Wordle Instructions',' Slime Jump Instructions', '             Settings', '              Wordle', '           Slime Jump', '          Scoreboard1','          Scoreboard2' ,'                Exit']
title_main = "Game Menu"

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

#wordle images 
bg_before=pygame.image.load('final_game\images\wordlebackground.jpg')
background = pygame.transform.scale(bg_before, (700,600))
win_before=pygame.image.load('final_game\images\winning.png')
win = pygame.transform.scale(win_before, (700,600))

#Slime Jump Images
slime1_before = pygame.image.load('final_game\images\slimejumpimages\slime1.1.png')
slime1 = pygame.transform.scale(slime1_before, (75, 60))
slime2 = pygame.image.load('final_game\images\slimejumpimages\slime2.2.png')
slime3 = pygame.image.load('final_game\images\slimejumpimages\slime3.3.png')
bg_before = pygame.image.load('final_game\images\cloud.jfif')
bg = pygame.transform.scale(bg_before, (700, 600))

#wordle stuff (board, fonts, words, other variables)
board = [[" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],]
LETTER_FONT = pygame.font.SysFont('comicsans', 55)
win_font = pygame.font.SysFont('comicsans', 45)
again_font = pygame.font.SysFont('comicsans', 20)
turn = 0
letters = 0
turn_now = True
game_over = False
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

#Slime Jump Stuff (font, platforms, score, other variables)
SCORE_FONT = pygame.font.SysFont('comicsans', 30)
score = 0
high = 0 
game_over1 = False
player_x = 300
player_y = 380
platforms = [[270,550,150,10], [70, 450, 150, 10], [470, 450, 150, 10], [270,350,150,10],[70,250,150,10], [470,250,150,10]]
jump = False
y_change = 0 
x_change = 0
player_speed = 3

def mainMenu(Title, message, MENU):
    global menu_color #have to import undefined variables 
    text_title = TITLE_FONT.render(Title, 1, colors.get("blue")) 
    screen.fill(menu_color)
    xd = WIDTH//2- (text_title.get_width()//2) #to make center by putting width//2 minus the space the words take
    screen.blit(text_title, (xd, 50))
    yMenu=150
    
    for item in message: #making buttons for Menu 
        Button_menu=pygame.Rect(bx, yMenu, WIDTH//3, 40)
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        pygame.draw.rect(screen, colors.get('pink'), Button_menu)
        screen.blit(text, (bx, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
    
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #exit screen if press x
                #bye-bye screen
                text_title = TITLE_FONT.render("Bye-Bye", 1, colors.get("blue")) 
                screen.fill(menu_color)
                screen.blit(text_title, (WIDTH//2-80,HEIGHT//2-100)) 
                pygame.display.update()
                pygame.time.delay(2000) #show bye-bye screen for 2 seconds
                pygame.quit()
                sys.exit()

            #making collidepoints for Menu options
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

    #bring in settings file and read it
    myFile = open("final_game\settings.txt", "r") 
    content = myFile.readlines()
    myFile.close()

    yi = 100
    for line in content: #size and color of words in file
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
    d = HEIGHT//2 -30
    e = HEIGHT//6 +300
    screen.blit(Title2, (xd, 50))
    screen.blit(text2, (480,HEIGHT//6+405))
    screen.blit(text3, (a+55,d))
    screen.blit(text4, (a+255,d))
    screen.blit(text5, (b-40,d-100))
    screen.blit(text6, (c+20,e))
    screen.blit(text7, (c+195,e))
    screen.blit(text8, (c+375,e))

    pygame.display.update()

    while True: #making colidepoints for each button in settings and x button
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
            
def readFile(titleF, fileN): #making code for any file I open 
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

    #Instructions of opening and reading file
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
        for event in pygame.event.get(): #if press x or return button go back to main menu 
            if event.type==pygame.QUIT:
                mainMenu(title_main, message_menu, True)
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu(title_main, message_menu, True)

    #making words for buttons/title
    title=TITLE_FONT.render('Scoreboard', 1, colors.get('blue'))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("blue"))

    # Making buttons and placement of them
    screen.fill(menu_color)
    Button_3 = pygame.Rect(450, 600, 200, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_3)
    screen.blit(title, (WIDTH//3,50))
    screen.blit(text3, (480,605))
    pygame.display.update()

def Game_1(): 
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
        global board, random_word, turn, letters, turn_now, game_over, background
        clock.tick(fpr) #making game run for 60 frames per minute
        screen.blit(background,(0,0)) #making background CHANGE LATER
        check_word() #put check word first so the green/yellow box are under what you right
        draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if press x will take back to menu
                mainMenu(title_main, message_menu, True) #something wrong HERE
                wordle = False
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
                    date = datetime.datetime.now()
                    scrLine=str(turn)+('      ')+ ("Christan") + ('      ') + date.strftime("%m-%d-%Y")+ "\n"
                    myFile = open("final_game\wordleScore.txt", "a")
                    myFile.write(str(scrLine))
                    myFile.close() 
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
                screen.fill(colors.get('white'))
                lose_text = LETTER_FONT.render("You lost", True, colors2.get('black'))
                screen.blit(lose_text, (WIDTH//2 -100,HEIGHT//2-150))
                word = ("The word was " + random_word)
                word_text = win_font.render( word, True, colors2.get('black'))
                screen.blit(word_text, (WIDTH//2 - 200,HEIGHT//2-50))
                playagain_text = again_font.render("To play again press 'enter' and to stop play press the x", 1, colors2.get('black'))
                screen.blit(playagain_text, (WIDTH//2 - 250,HEIGHT//6-80))
                scoreinfo_text = again_font.render("Press enter to save score", 1, colors2.get('black'))
                screen.blit(scoreinfo_text, (WIDTH//2 - 125,HEIGHT//6-50))

            if game_over and turn < 7 and guess == random_word: #have to use 'and' and not game_over = True becuase game starts like that if do game wont play 
                screen.blit(win,(0,0))
                win_text = win_font.render("You Win!", True, colors2.get('black'))
                screen.blit(win_text, (WIDTH//2 -90,HEIGHT//2-170))
                word = ("The word was " + random_word)
                word_text = win_font.render( word, True, colors2.get('black'))
                screen.blit(word_text, (WIDTH//2 - 200,HEIGHT//2+220))
                playagain_text = again_font.render("To play again press 'enter' and to stop play press the x", 1, colors2.get('black'))
                screen.blit(playagain_text, (WIDTH//2 - 250,HEIGHT//6-80))
                scoreinfo_text = again_font.render("Press enter to save score", 1, colors2.get('black'))
                screen.blit(scoreinfo_text, (WIDTH//2 - 125,HEIGHT//6-50))

        pygame.display.flip()

def Game_2():
   #check for collision with blocks 
    def check_collisions(rect_list, j): #checking if rect_list = platforms and j= jump hit 
        global player_x, player_y, y_change
        for i in range(len(rect_list)): 
            if rect_list[i].colliderect([player_x, player_y+60, 90, 5]) and jump == False and y_change > 0: #checks is rect collides when jump == false and player is falling 
                j = True
        return j

    #update user y positions every loop 
    def update_player(y_pos): #finding y position to know when to scroll screen up 
        global jump, y_change
        jump_height = 11 #how high the slime will jump
        gravity = 0.5 #how quickly it comes down 
        if jump: #send player jumping but then immidietly bring back down 
            y_change = -jump_height
            jump = False
        y_pos += y_change
        y_change += gravity #gravity affects immidietetly 
        return y_pos

    #handle movement of platforms as game progresses 
    def update_platforms(my_list, y_pos, change): #getting randomized platforms 
        global score
        if y_pos < 250 and change < 0: #only when you are jumping and hit position fo 250 will the screen go up
            for i in range(len(my_list)):
                my_list[i][1] -= change
        else:
            pass 
        for item in range(len(my_list)):
            if my_list[item][1] > 600: #create when screen hit x = 600 
                my_list[item] = [random.randint(50,520), random.randint(250,300), 100,10] #randomize platform x and y positions
                score += 1 
        return my_list
    
    Slime_Jump = True  #game part 
    while Slime_Jump:
        global slime1, slime1_before, player_x, player_y, bg, fpr, score, score_text, platforms, block, x_change, y_change, high, jump
        clock.tick(fpr)
        screen.blit(bg,(0,0))
        screen.blit(slime1,(player_x, player_y))
        blocks = []
        #top right with scores
        score_text = SCORE_FONT.render('Score: '+ str(score), True, colors2.get('black'), colors.get('white')) 
        screen.blit(score_text, (530,20))
        highscore_text = SCORE_FONT.render('High Score: '+ str(high), True, colors2.get('black'), colors.get('white'))
        screen.blit(highscore_text, (490,60))

        for i in range(len(platforms)): #drawing first 7 platforms before random      # 0,5 makes it round and filled in 
            block = pygame.draw.rect(screen, colors2.get('black'), platforms[i], 0,5) #[i] making length height corrdinates as platform []
            blocks.append(block)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #if press x go to menu and stop game 
                mainMenu(title_main, message_menu, True)
                Slime_Jump = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over1: #if press space start game over and bring to starting position
                    date = datetime.datetime.now()
                    scrLine=str(score)+('      ')+ ("Christan") + ('      ') + date.strftime("%m-%d-%Y")+ "\n"
                    myFile = open("final_game\slimpJumpScore.txt", "a")
                    myFile.write(str(scrLine))
                    myFile.close()
                    slime1 = pygame.transform.scale(slime1_before, (75,60)) 
                    game_over1 = False
                    score = 0
                    player_x = 300
                    player_y = 380
                    platforms = [[270,550,150,10], [70, 450, 150, 10], [470, 450, 150, 10], [270,350,150,10],[70,250,150,10], [470,250,150,10]]
                    screen.blit(bg,(0,0))
                if event.key == pygame.K_LEFT: #if press left arrow x will change depending on player speed 
                    x_change = -player_speed #negative bc x has to become less to go left
                if event.key == pygame.K_RIGHT:
                    x_change = player_speed #positive bc x has to be higher to move right 
            if event.type == pygame.K_UP:
                if event.key == pygame.K_LEFT:
                    x_change = 0 #when they let go the change will be 0 to stop going left or right and stay in one place
                if event.key == pygame.K_RIGHT:
                    x_change = 0

        jump = check_collisions(blocks, jump) #making each time they jump = jumping and chekcing collisions with platforms 
        player_x += x_change #player_x positon + x_change made before with left and right arrows 

        if player_y <640: 
            player_y = update_player(player_y) #use to control up and down movement 
        else:
            game_over1 = True
            y_change = 0
            x_change = 0
        platforms = update_platforms(platforms, player_y, y_change) #lets you know how much you need to modify loction fo platforms 
        
        #setting boundries so the slime can fall off right and left edges instead of stop against edge 
        if player_x < -70: 
            player_x = -70 
        elif player_x > 625:
            player_x = 625

        #making when going left and right the slime character changes too 
        if x_change > 0:
            slime1 = pygame.transform.scale(slime2, (75,60)) 
        if x_change < 0:
            slime1 = pygame.transform.scale(slime3, (75,60))

        if score > high:
            high = score 
        
        pygame.display.flip()

def name(): #making computer ask user name 
    screen.fill(menu_color)
    run = True 
    user_name = ''
    nameClr = (0,105,105)
    bxClr = (200,200,200)

    #making title and position of it
    title = TITLE_FONT.render("Enter name ", 1, bxClr)
    screen.blit(title, (WIDTH//2-100,200))
    pygame.time.delay(500)
    pygame.display.update()
    
    #box to write in
    name_box = pygame.Rect(WIDTH/2-90, HEIGHT//2, 200, 50)

    while run:
        for event in pygame.event.get():
                if event.type==pygame.QUIT: #if press x go back to menu
                    mainMenu(title_main, message_menu, True)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    #making box 
                    name_box = pygame.Rect(WIDTH/2-90, HEIGHT//2, 200, 50)
                    pygame.draw.rect(screen, colors.get("white"), name_box)
                    pygame.display.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: #when press enter goes to menu 
                        mainMenu(title_main, message_menu, True)
                    if event == pygame.K_BACKSPACE: #allows user to delete past letters to fix mistakes if made one
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

def exit(): #when press x from menu close screen 
    title=TITLE_FONT.render('Bye-Bye', 1, colors.get('blue')) #making words
    screen.fill(menu_color) #making background color
    screen.blit(title, (WIDTH//2-80,HEIGHT//2-100)) #making placement of words
    pygame.display.update() #updating screen to show up
    pygame.time.delay(1000) #stays there for a second 
    pygame.quit() #close pygame
    sys.exit() #closes entire system

name()
mainMenu(title_main, message_menu, True)