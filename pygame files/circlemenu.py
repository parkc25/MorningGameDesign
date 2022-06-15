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
from turtle import title, width
import pygame, time,os,random, math
import datetime
pygame.init()#initialize the pygame package

# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
colors2 = {"grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
clr=colors.get("limeGreen")
message=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window

 #creating buttons
Button_instruct = pygame.Rect(25, 150, 40, 40)
Button_settings = pygame.Rect(25, 200, 40, 40)
Button_game1 = pygame.Rect(25, 250, 40, 40)
Button_game2 = pygame.Rect(25, 300, 40, 40)
Button_score = pygame.Rect(25, 350, 40, 40)
Button_exit = pygame.Rect(25, 400, 40, 40)

#images
bg=pygame.image.load('pygame files\Images\pygame background.jpg')
char = pygame.image.load('pygame files\Images\\alien.jpg')
ball = pygame.image.load("pygame files\Images\\ball.png")
char = pygame.transform.scale(char, (50, 50))
ball_size = pygame.transform.scale(ball, (50,50))
square = pygame.Rect(50,50,100,300)
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#square Var
hb=50
wb=50
xb=100
yb=300

charx = xb
chary = yb
squarex = xb
squarey =yb

cx=350
cy=350
rad=25
speed=2
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

def mainMenu():
    pygame.draw.rect(screen, colors.get('pink'), Button_settings)
    Title = TITLE_FONT.render("Circle eats Square Menu", 1, colors.get("blue"))
    screen.fill(colors.get('white'))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    yMenu=150
    
    for item in message:
        Button_menu=pygame.Rect(50, yMenu, 40, 40)
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        pygame.draw.rect(screen, colors.get('pink'), Button_menu)
        screen.blit(text, (110, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
    
    MENU=True
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("You quit")
                pygame.display.quit()
                MENU=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_instruct.collidepoint((mx, my)):
                    readFile("Instructions", "pygame files\instruction.txt")
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_game1.collidepoint((mx, my)):
                    Game_1()
                if Button_game2.collidepoint((mx, my)):
                    level_2()
                if Button_score.collidepoint((mx, my)):
                    readFile("Score Board", "pygame files\score.txt")
                if Button_exit.collidepoint((mx, my)):
                    exit()
                if Button_exit.collidepoint((mx, my)):
                    textTitle = TITLE_FONT.render("Bye-Bye", 1, colors.get("blue"))
                    name = "Christan" 
                    sce = 300 
                    date=datetime.datetime.now()
                    scrLine = str(sce) + "     " + name + "     " + date.strftime("%m-%d-%Y") + "\n"
                    myFile = open("score.txt", 'a')
                    myFile.write(scrLine)
                    myFile.close()
                    screen.fill(colors.get('white'))
                    xd = WIDTH//2 - (textTitle.get_width()//2)
                    yd = HEIGHT//2 - 40
                    screen.blit(textTitle, (xd, yd))
                    pygame.display.update()

def settings():
    Title2=TITLE_FONT.render('Settings', 1, colors.get('blue'))
    text2=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
    text3=MENU_FONT.render('On', 1, colors.get('blue'))
    text4=MENU_FONT.render('Off', 1, colors.get('blue'))
    screen.fill(colors.get('white'))

    myFile = open("pygame files\settings.txt", "r")
    content = myFile.readlines()

    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    Button_2 = pygame.Rect(450, 600, 200, 50)
    Button_red = pygame.Rect(150, 220, 50, 50)
    Button_orange = pygame.Rect(220, 220, 50, 50)
    Button_yellow = pygame.Rect(290, 220, 50, 50)
    Button_green = pygame.Rect(360, 220, 50, 50)
    Button_purple = pygame.Rect(430, 220, 50, 50)
    Button_grey = pygame.Rect(500, 220, 50, 50)
    Button_sound_on = pygame.Rect(175, 360, 150, 50)
    Button_sound_off = pygame.Rect(375, 360, 150, 50)

    pygame.draw.rect(screen, colors.get("pink"), Button_2)
    pygame.draw.rect(screen, colors2.get("red"), Button_red)
    pygame.draw.rect(screen, colors2.get("orange"), Button_orange)
    pygame.draw.rect(screen, colors2.get("yellow"), Button_yellow)
    pygame.draw.rect(screen, colors2.get("green"), Button_green)
    pygame.draw.rect(screen, colors2.get("purple"), Button_purple)
    pygame.draw.rect(screen, colors2.get("grey"), Button_grey)
    pygame.draw.rect(screen, colors.get("pink"), Button_sound_on)
    pygame.draw.rect(screen, colors.get("pink"), Button_sound_off)

    xd = WIDTH//2 - (Title2.get_width()//2)
    screen.blit(Title2, (xd, 50))
    screen.blit(text2, (480,605))
    screen.blit(text3, (235,370))
    screen.blit(text4, (430,370))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                mainMenu()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_2.collidepoint((mx, my)):
                    mainMenu()
                if Button_red.collidepoint((mx,my)):
                    screen.fill(colors2.get('red'))
                if Button_orange.collidepoint((mx,my)):
                    screen.fill(colors2.get('orange'))
                if Button_yellow.collidepoint((mx,my)):
                    screen.fill(colors2.get('yellow'))
                if Button_green.collidepoint((mx,my)):
                    screen.fill(colors2.get('green')) 
                if Button_purple.collidepoint((mx,my)):
                    screen.fill(colors2.get('purple'))
                if Button_grey.collidepoint((mx,my)):
                    screen.fill(colors2.get('grey'))

def readFile(titleF, fileN):
    screen.fill(colors.get('white'))
    Title=TITLE_FONT.render(titleF, 1, colors.get('blue'))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd,50))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("blue"))

    Button_3 = pygame.Rect(450, 600, 200, 50)
    pygame.draw.rect(screen, colors.get("pink"), Button_3)


    #Instructions
    myFile = open(fileN, "r")
    content = myFile.readlines()
    myFile.close()

    #var to controll change of line
    yinstructions = 105
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
                run=False
                mainMenu()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()

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
    title=TITLE_FONT.render('Game Level 1', 1, colors.get('blue'))
    screen.fill(colors.get('white'))

    screen.blit(title, (275,50))
    pygame.display.update()
    score=0
    Game=True
    while Game:
        pygame.draw.rect(screen, colors.get("white"), mountainSquare)
        screen.fill(colors2.get('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                mainMenu()
                print("you quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                # print(mousePos)
        keys = pygame.key.get_pressed() #allow us to see what key was pressed

        #square movement
        if keys[pygame.K_d] and square.x < WIDTH-wb:
            square.x += speed
            squarex += speed
        if keys[pygame.K_a] and square.x > 0:
            square.x -= speed
            squarex -= speed
        if keys[pygame.K_s] and square.y < HEIGHT-hb:
            square.y += speed
            squarey += speed
        if keys[pygame.K_w] and square.y > 0:
            square.y -= speed
            squarey -= speed

        #circle and inscribed square movement
        if keys[pygame.K_RIGHT] and cx < WIDTH-rad:
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_LEFT] and cx > 0+rad:
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_DOWN] and cy < HEIGHT-rad:
            cy += speed
            insSquare.y += speed
        if keys[pygame.K_UP] and cy > 0+rad:
            cy -= speed
            insSquare.y -= speed
        
        #circle square collide
        if square.colliderect(insSquare): 
            print("BOOM")
            score += 5
            cx = WIDTH +5
            cy = HEIGHT +5 
            rad += 5
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        
        #mountain collide square
        if square.colliderect(mountainSquare):
            square.x = 10
            square.y = 10
            squarex = 10
            squarey = 10
        
        #mountain collide circle
        if insSquare.colliderect(mountainSquare):
            rad += 5
            cx = rad + 10
            cy = rad + 10
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)

        #rect(surface, color, object)
        pygame.draw.rect(screen, colors.get("blue"), insSquare)
        pygame.draw.rect(screen, colors.get("blue"), square)

        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, colors.get("pink"), (cx, cy), rad)
        
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
                mainMenu()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()

def level_2():
    global score, hb, wb, xb, rad, yb, squarex, squarey, cx, cy, speed, ibox, xig, yig, char, bg, mx, my, insSquare
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
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, colors2.get("yellow"),square)
        screen.blit(char, (squarex, squarey))
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, colors.get("white"), (cx,cy), rad)
        pygame.draw.rect(screen, colors2.get("orange"), insSquare)
        pygame.display.update()
        pygame.time.delay(5)

mainMenu()