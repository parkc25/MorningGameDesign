#Christan Park
#6/15/2022
#TicTacToe game 

#Funtion to draw grid:
#draw_grid()
#zero_grid()
#draw_markers() -> time to draw x and o
#check_winner()
#play again? 

import pygame, time,os,random, math, sys, datetime
pygame.init()#initialize the pygame package
os.system('cls')

WIDTH=600 #like constant
HEIGHT=600
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Tik Tac Tow")  #change the title of my window

colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}

SIZE = 3
markers = []
MxMy = (0,0)
line_width = 10 
cellx = 0 
celly = 0
player = 1
circle_color = colors.get("red")
x_color = colors.get("green")

def zero_grid():
    for x in range(SIZE):
        row=[0]*SIZE #this will create 3 zeros 
        markers.append(row)

# zero_grid()
# print(markers)
# markers[1][1]=-1 #first indez in row sec in col
# print(markers)
# print(markers[1][1])

def draw_grid():
    background_color = colors.get("white")
    line_color = colors.get("blue")
    screen.fill(background_color)
    for x in range(1,3):
        pygame.draw.line(screen, line_color,(0,HEIGHT//3*x),(WIDTH, HEIGHT//3*x), line_width) #horizonal lines
        pygame.draw.line(screen, line_color,(WIDTH//3*x, 0),(WIDTH//3*x, HEIGHT), line_width)
        pygame.display.update()

def draw_markers():
    global line_width, xValue, yValue
    xValue = 0
    for x in markers: #give me each row
        yValue = 0
        for y in x: #give me each column
            if y == 1:
                #draw x
                pygame.draw.line((xValue*WIDTH//3+15, yValue*HEIGHT//3+15),(xValue*WIDTH//3+WIDTH//3-15, yValue*HEIGHT-15), line_width)
            if y == -1:
                #draw o 
                pygame.draw.circle(screen, circle_color, (xValue*WIDTH//3+WIDTH//6+5, yValue*HEIGHT//3+HEIGHT//6), WIDTH, line_width)



zero_grid()
Game = True 
while Game:
    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        MxMy = pygame.mouse.get_pos()
        cellx = MxMy[0]//(WIDTH//SIZE)
        celly = MxMy[1]//(HEIGHT//SIZE)
        print(markers)
        if markers[cellx][celly]==0:
            markers[cellx][celly]=player
            player += 1
