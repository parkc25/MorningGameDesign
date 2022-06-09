#Christan Park 
# June 9th, 2022 
#we are learning pygame's basic functions, 
#creating screen, clrs, and shapes 

from operator import truediv
import os
os.system('cls')

import pygame, time
pygame.init() #initialize the pygame package 

#making dimentions 
WIDTH = 700 #like a constant 
HEIGHT = 700
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
square = (xb,yb,wb,hb) #creat the object to draw
backgroundColor = greenColor
run = True
while run: 
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
            print("Y quit")

    ##rect(surface, color, rect)
    pygame.draw.rect(screen, blueColor, square)
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, purpleColor, [350,350], 25)
    pygame.display.update()
