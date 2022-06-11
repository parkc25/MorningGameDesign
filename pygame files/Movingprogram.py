#Christan Park 
# June 9th, 2022 
#we are learning pygame's basic functions, 
#creating screen, clrs, and shapes 
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow

import os
import pygame, time
import random
import math
pygame.init()# this initialize the pygame package 
os.system("cls")

WIDTH=700 #like constant 
HEIGHT=700 #this are also the parameters of teh screen/display 
#create display window with any name you like 
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("my first game")#this change the title of the pygame screen 
bg=pygame.image.load('pygame files\Images\pygame background.jpg')
char=pygame.image.load('pygame files\Images\character image.png')
char= pygame.transform.scale(char,(64,64))
# screen.blit(bg,(0,0))
# pygame.display.update
# pygame.time.delay(5000)
# #pygame.time.delay(2000)#this maes the screen stay for the amount of time you define 
redClr=(255,0,0)#sets a color value 
#screen.fill(redClr)#command to fill teh screen 
#pygame.display.update()#must update every time u change the display 
#pygame.time.delay(2000)
color={"white":(255,255,255),"limegreen":(153,255,51),"pink":(255,0,255),"blue":(0,0,255),"yellow":(255,255,0),"purple":(102,0,204)} #can store a bunch of colors in a list 
clr=color.get("limegreen")
greenClr=(0,255,0)
purpleClr=(125,0,125)
squareclr=color.get("pink")
circleclr=color.get("blue")
#screen.fill(greenClr)
#pygame.display.update()
#pygame.time.delay(2000)
#to keep this running u must create a loop 
cx=350
cy=350
rad=25
ibox=rad*math.sqrt(2)
xig= cx-(ibox/2)
yig= cy-(ibox/2)
inscribSq=pygame.Rect(xig,yig,ibox,ibox)
hb=50
wb=50
xb=100
yb=300
charx=xb
chary=yb
square=pygame.Rect(xb,yb,wb,hb) #creates the object t draw

backgrnd=color.get("limegreen")
speed=2

run = True
while run:
    screen.blit(bg,(0,0))
    #screen.fill(backgrnd)
    for event in pygame.event.get(): #will create a reaction for everything that happens with mouse or keybord
        if event.type==pygame.QUIT:
            run=False 
            print("y quit da game ")
    keys= pygame.key.get_pressed() #this is a list 
    if keys[pygame.K_RIGHT] and square.x <WIDTH -(wb+speed):
        square.x +=speed 
        charx+=speed
    if keys[pygame.K_LEFT] and square.x > speed:
        square.x-=speed
        charx-=speed
    if keys[pygame.K_UP] and square.y >speed:
        square.y -=speed
        chary-=speed
    if keys[pygame.K_DOWN] and square.y <HEIGHT-hb:
        square.y +=speed
        chary+=speed
    #this will move the circle 
    if keys[pygame.K_d]and cx <WIDTH -(rad):
        cx +=speed
        inscribSq.x+=speed
    if keys[pygame.K_a] and cx > (speed+rad):
        cx-=speed
        inscribSq.x-=speed
    if keys[pygame.K_w] and cy > (speed+rad):
        cy -=speed
        inscribSq.y-=speed
    if keys[pygame.K_s] and cy <HEIGHT-(rad):
        cy +=speed
        inscribSq.y+=speed
    if square.colliderect(inscribSq):
        print("BOOM")
        rad+=5
        cx=random.randint(rad, WIDTH-rad)  
        cy=random.randint(rad, HEIGHT-rad)  
        ibox=rad*math.sqrt(2)
        xig= cx-(ibox/2)
        yig= cy-(ibox/2)
        inscribSq=pygame.Rect(xig,yig,ibox,ibox)
    pygame.draw.rect(screen,squareclr,square) #to make the rectange you need teh surface, the color and the shape
    #circle (surface color center radius)
    screen.blit(char,(300,300))
    pygame.draw.circle(screen,circleclr,(cx,cy),rad)
    pygame.draw.rect(screen, squareclr, inscribSq)
    pygame.display.update()