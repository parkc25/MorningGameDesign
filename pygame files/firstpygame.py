#Christan Park 
# June 9th, 2022 
#we are learning pygame's basic functions, 
#creating screen, clrs, and shapes 
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
#picture = pygame. image. load(filename)
#picture = pygame. transform. scale(picture, (1280, 720))
#bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')

from operator import truediv
import os
from random
from turtle import width
os.system('cls')

import pygame
import time
pygame.init() #initialize the pygame package 

#making dimentions 
WIDTH = 700 #like a constant 
HEIGHT = 700
colors = {'white':(255,255,255), 'pink':(255,0,255), 'blue': (0,204,204)}
clr = colors.get('white')
#creating display window with any name you want
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame") #change title of the window
pygame.time.delay(1000) #set time the window shows up 
redColor = (255,0,0)
#screen.fill(redColor)
#pygame.display.update()
#pygame.time.delay(1000)
greenColor = (0,255,0)
#screen.fill(greenColor)
#pygame.display.update()
#pygame.time.delay(1000)
blueColor = (0,0,255)
#screen.fill(blueColor)
#pygame.display.update()
#pygame.time.delay(1000)
#to make it keep running create a loop 
purpleColor = (125,0,125)
hb = 50 
wb = 50 
xb = 100
yb = 300
square = pygame.Rect(xb,yb,wb,hb) #creat the object to draw
hb = 100 
wb = 100
xb = 200
yb = 200
ab = 150 
ac = 150
ba = 250 
bb = 250 
ca = 300 
cb = 300
polygon = [(xb,yb),(wb,hb),(ab,ac), (ba, bb), (ca,cb)]
rad = 25
cx = 350
cy = 350 
backgroundColor = clr
run = True
speed=2
while run: 
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
            print("Y quit")

#move square
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and square.x < WIDTH - wb:
        square.x += speed
    if keys[pygame.K_LEFT] and  square.x > speed:
        square.x -= speed
    if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
        square.y -= speed
    if keys[pygame.K_DOWN] and square.y <HEIGHT - hb:  #means clser t max value HEIGHT
        square.y += speed

#move circle 
    keys = pygame.key.get_pressed() #have to make variables for circle becuase it can only be drawn 
    if keys[pygame.K_d] and cx <WIDTH - (rad):
        cx += speed
    if keys[pygame.K_a] and cx> (speed+rad):
        cx -= speed
    if keys[pygame.K_w] and cy > (speed+rad):
        cy -= speed
    if keys[pygame.K_s] and cy < HEIGHT -(rad):
        cy += speed
    if square.collidepoint(cx,cy):
        print("BOOM!")
        cx.random.radiant(rad, WIDTH-rad)
        cy.random.radiant(rad, HEIGHT-rad)

    ##rect(surface, color, rect)
    pygame.draw.rect(screen, blueColor, square)
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, purpleColor, (cx,cy), rad)
    pygame.draw.polygon(screen, redColor, polygon)
    pygame.display.update()

