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
HEIGHT=700
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
score = 0

#colors for game
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
colors2 = {"grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}

#background colors
menu_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

message_menu=['          Instructions', '             Settings', '              Game 1', '              Game 2', '          Scoreboard', '                Exit']
title_main = "Circle Eats Square Menu"

#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Circle Square Game")  #change the title of my window

#creating buttons
bx = WIDTH//3
Button_instruct = pygame.Rect(bx, 150, WIDTH//4, 40)
Button_settings = pygame.Rect(bx, 200, WIDTH//4, 40)
Button_game1 = pygame.Rect(bx, 250, WIDTH//4, 40)
Button_game2 = pygame.Rect(bx, 300, WIDTH//4, 40)
Button_score = pygame.Rect(bx, 350, WIDTH//4, 40)
Button_exit = pygame.Rect(bx, 400, WIDTH//4, 40)

#images
bg=pygame.image.load('pygame files\Images\pygame background.jpg')
char = pygame.image.load('pygame files\Images\\alien.jpg')
char = pygame.transform.scale(char, (50, 50))
square = pygame.Rect(50,50,100,300)
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#background sound
mixer.music.load("pygame files\CircleMenu\\background.wav")
mixer.music.play(-1)

#square Var
hb=50
wb=50
xb=100
yb=300

#char var
charx = xb
chary = yb

#square for game1 var
squarex = xb
squarey =yb

#circle var
cx=350
cy=350
rad=25

speed=2

#inscribed squared var
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse varuables
mx = 0
my = 0

square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
insSquare=pygame.Rect(xig,yig,ibox,ibox)
squareClr=colors.get("pink")
#keep running create a lp
mountainSquare=pygame.Rect(250,320,180,250)
circleClr=colors.get("blue")
backgrnd=colors.get("limeGreen")
run = True
Game = False

def mainMenu(Title, message, MENU):
    global menu_color
    text_title = TITLE_FONT.render(Title, 1, colors.get("blue"))
    screen.fill(menu_color)
    xd = WIDTH//2- (text_title.get_width()//2)
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
                text_title = TITLE_FONT.render("Bye-Bye", 1, colors.get("blue"))
                screen.fill(menu_color)
                xd = WIDTH//2 - (text_title.get_width()//2)
                yd = HEIGHT//2-40
                screen.blit(text_title, (xd, yd))
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_instruct.collidepoint((mx, my)):
                    readFile("Instructions", "pygame files\CircleMenu\instruction.txt")
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_game1.collidepoint((mx, my)):
                    Game_1()
                if Button_game2.collidepoint((mx, my)):
                    Game_2()
                if Button_score.collidepoint((mx, my)):
                    print(score)
                    date = datetime.datetime.now()
                    scrLine=str(score)+('      ')+ ("Christan") + ('      ') + date.strftime("%m-%d-%Y")+ "\n"
                    myFile = open("pygame files\CircleMenu\score.txt", "a")
                    myFile.write(str(scrLine))
                    myFile.close()
                    readFile("Scoreboard", "pygame files\CircleMenu\score.txt")
                if Button_exit.collidepoint((mx, my)):
                    exit()

def settings():
    global menu_color, screen, WIDTH, HEIGHT
    screen.fill(menu_color)
    Title2=TITLE_FONT.render('Settings', 1, colors.get('blue'))
    text2=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
    text3=MENU_FONT.render('On', 1, colors.get('blue'))
    text4=MENU_FONT.render('Off', 1, colors.get('blue'))
    text5=MENU_FONT.render('Random', 1, colors.get('blue'))
    text6=MENU_FONT.render('Original Size', 1, colors.get('blue'))
    text7=MENU_FONT.render('Width +100', 1, colors.get('blue'))
    text8=MENU_FONT.render('Width-100', 1, colors.get('blue'))

    myFile = open("pygame files\CircleMenu\settings.txt", "r")
    content = myFile.readlines()
    myFile.close()

    yi = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yi))
        pygame.display.update()
        # pygame.time.delay(50)
        yi += 40

    Button_2 = pygame.Rect(450, 600, 200, 50)
    Button_color = pygame.Rect(250, 220, 200, 50)
    Button_sound_on = pygame.Rect(175, 360, 150, 50)
    Button_sound_off = pygame.Rect(375, 360, 150, 50)
    Button_size0 = pygame.Rect(100, 520, 150, 50)
    Button_size1 = pygame.Rect(275, 520, 150, 50)
    Button_size2 = pygame.Rect(450, 520, 150, 50)

    pygame.draw.rect(screen, colors.get("pink"), Button_2)
    pygame.draw.rect(screen, colors.get("pink"), Button_color)
    pygame.draw.rect(screen, colors.get("pink"), Button_sound_on)
    pygame.draw.rect(screen, colors.get("pink"), Button_sound_off)
    pygame.draw.rect(screen, colors.get("pink"), Button_size0)
    pygame.draw.rect(screen, colors.get("pink"), Button_size1)
    pygame.draw.rect(screen, colors.get("pink"), Button_size2)

    xd = WIDTH//2 - (Title2.get_width()//2)
    screen.blit(Title2, (xd, 50))
    screen.blit(text2, (480,605))
    screen.blit(text3, (235,370))
    screen.blit(text4, (430,370))
    screen.blit(text5, (310,230))
    screen.blit(text6, (115,530))
    screen.blit(text7, (300,530))
    screen.blit(text8, (475,530))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                mainMenu(title_main, message_menu, True)
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_2.collidepoint((mx, my)):
                    mainMenu(title_main, message_menu, True)
                if Button_color.collidepoint((mx,my)):
                    menu_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    print("change color")
                if Button_sound_on.collidepoint((mx,my)):
                    mixer.music.play(-1)
                    print("music on")
                if Button_sound_off.collidepoint((mx,my)):
                    mixer.music.stop()
                    print("music off")
                if Button_size0.collidepoint((mx,my)):
                    screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
                if Button_size1.collidepoint((mx,my)) and WIDTH < 1100:
                    WIDTH+=100
                    screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
                if Button_size2.collidepoint((mx, my)) and WIDTH > 600: 
                    WIDTH-=100
                    screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
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
    Button_3 = pygame.Rect(450, 600, 200, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_3)


    #Instructions
    myFile = open(fileN, "r")
    content = myFile.readlines()
    myFile.close()

    #var to controll change of line
    yinstructions = 120
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()
    
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    screen.blit(text3, (480,605))
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
    
    print(score)
    # if score>high:
    #     high=score
    # scrLine=str(high)+"\t " (':')+ "\t" +date.strftime('%m/%d/%Y')+ "\n"
    date = datetime.datetime.now()
    scrLine=str(score)+('      ')+ ("Christan") + ('      ') + date.strftime("%m-%d-%Y")+ "\n"
    myFile = open("pygame files\CircleMenu\score.txt", "a")
    myFile.write(str(scrLine))
    myFile.close()

    myFile=open('pygame files\CircleMenu\score.txt', 'r')
    content = myFile.readlines()

    #var to controll change of line
    yscore = 150
    for lines in content:
        Instruc = MENU_FONT.render(lines[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yscore))
        pygame.display.update()
        pygame.time.delay(50)
        yscore += 40

    myFile.close()

    scoreboard=True
    while scoreboard:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu(title_main, message_menu, True)

def exit():
    title=TITLE_FONT.render('Bye-Bye', 1, colors.get('blue'))
    screen.fill(colors.get('white'))
    screen.blit(title, (275,200))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()                

def Game_1():

    global score, hb, wb, xb, rad, yb, squarex, squarey, cx, cy, speed, ibox, xig, yig, char, bg, mx, my, insSquare
    score = 0
    title=TITLE_FONT.render('Game Level 1', 1, colors.get('blue'))
    screen.fill(colors.get('white'))

    screen.blit(title, (275,50))
    pygame.display.update()
    score=0
    Game=True
    while Game:
        screen.fill(colors2.get('black'))
        # screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                mainMenu(title_main, message_menu, True)
                run=False
                print("Y quit")
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
            square.x += speed
            squarex += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            squarex -= speed
        if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
            square.y -= speed
            squarey -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
            square.y += speed
            squarey += speed
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
            cy += speed
            insSquare.y += speed

        if square.colliderect(insSquare):
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            score += 1
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, squareClr,square)
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, circleClr, (cx,cy), rad)
        pygame.draw.rect(screen, squareClr, insSquare)
        pygame.display.update()
        pygame.time.delay(5)

    title=TITLE_FONT.render('Scoreboard', 1, colors.get('blue'))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("blue"))

    screen.fill(colors.get('white'))
    Button_3 = pygame.Rect(25, 350, 200, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    
    screen.blit(title, (250,50))
    screen.blit(text3, (30, 355))
    pygame.display.update()
    
    print(score)
    File=open('pygame files\score.txt', 'a')
    File.write(str(score))
    File.close()

    scoreboard=True
    while scoreboard:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                mainMenu(title_main, message_menu, True)
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu(title_main, message_menu, True)

def Game_2():
    global score, hb, wb, xb, rad, yb, squarex, squarey, cx, cy, speed, ibox, xig, yig, char, bg, mx, my, insSquare
    score = 0
    title=TITLE_FONT.render('Game Level 1', 1, colors.get('blue'))
    screen.fill(colors.get('white'))

    screen.blit(title, (275,50))
    pygame.display.update()
    score=0
    Game=True
    while Game:
        screen.blit(bg, (0,0))
        # screen.fill(backgrnd)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                mainMenu(title_main, message_menu, True)
                run=False
                print("Y quit")
        keys= pygame.key.get_pressed() #this is a list
        #mve square
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
            square.x += speed
            squarex += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            squarex -= speed
        if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
            square.y -= speed
            squarey -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
            square.y += speed
            squarey += speed
            #mve Circle
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   #means clser t 0
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means clser t max value HEIGHT
            cy += speed
            insSquare.y += speed

        if square.colliderect(insSquare):
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            score += 1
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, colors2.get("yellow"),square)
        screen.blit(char, (squarex, squarey))
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, colors.get("white"), (cx,cy), rad)
        pygame.draw.rect(screen, colors2.get("orange"), insSquare)
        pygame.display.update()
        pygame.time.delay(5)

mainMenu(title_main, message_menu, True)