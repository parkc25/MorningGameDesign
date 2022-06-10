#Christan Park 
# June 9th, 2022 
#we are learning pygame's basic functions, 
#creating screen, clrs, and shapes 

from operator import truediv
import os
from random import random
os.system('cls')

import pygame, time
pygame.init() #initialize the pygame package 

#making dimentions 
WIDTH = 700 #like a constant 
HEIGHT = 700
colors = {'white':(255,255,255), 'pink':(255,0,255), 'blue': (0,204,204)}
colors2 = {'redColor' :(255,0,0), 'greenColor': (0,255,0) ,'blueColor': (0,0,255), 'purpleColor': (125,0,125)}
colors3 = {}
backgroundclr = colors.get('white')
circleclr = colors.get('pink')
squareclr = colors2.get('purple')
polygonclr = colors2.get('blue')
#creating display window with any name you want
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame") #change title of the window
pygame.time.delay(1000) #set time the window shows up 
hb = 50 
wb = 50 
xb = 100
yb = 300
square = pygame.Rect(xb,yb,wb,hb) #creat the object to draw
hb = 50 
wb = 100
xb = 100 
yb = 50
ab = 150 
ac = 200
ba = 200 
bb = 150
polygon = [(xb,yb),(wb,hb),(ab,ac), (ba, bb)]
backgroundColor = backgroundclr
run = True
#create varibale to move shapes 
speed = 2
while run: 
    screen.fill(backgroundColor)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
            print("Y quit")
    keys = pygame.key.get_pressed() #this is a list 
    if keys[pygame.K_RIGHT] and square.x <WIDTH - (wb):
        square.x += speed
    if keys[pygame.K_LEFT] and square.x> speed:
        square.x -= speed
    if keys[pygame.K_DOWN] and square.y > speed:
        square.y -= speed
    if keys[pygame.K_UP] and square.y < WIDTH -(wb):
        square.y += speed

##rect(surface, color, rect)
pygame.draw.rect(screen, squareclr, square)
#circle(surface, color, center, radius)
pygame.draw.circle(screen, circleclr, [350,350], 25)
pygame.draw.polygon(screen, polygonclr, polygon)
pygame.display.update()
