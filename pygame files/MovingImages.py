#Christan Park 
# Please watch the video
# Take notes the first time you watch it
# The second time, you should try to recreate the game as he explains it.
# Find some images that you may want to use for your game
import os 
os.system('cls')

import pygame
pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('pygame files\Images\Moving Images HW Images\R1.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\R2.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\R3.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\R4.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\R5.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\R6.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\R7.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\R8.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\R9.png')]
walkLeft = [pygame.image.load('pygame files\Images\Moving Images HW Images\L1.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\L2.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\L3.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\L4.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\L5.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\L6.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\L7.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\L8.png'), pygame.image.load('pygame files\Images\Moving Images HW Images\L9.png')]
bg = pygame.image.load('pygame files\Images\Moving Images HW Images\gb.jpg')
char = pygame.image.load('pygame files\Images\Moving Images HW Images\standing.png')

x = 50
y = 400
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update() 
    


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow() 
    
    
pygame.quit()