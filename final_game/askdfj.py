#Christan Park 
# Please watch the video
# Take notes the first time you watch it
# The second time, you should try to recreate the game as he explains it.
# Find some images that you may want to use for your game
import os, random
os.system('cls')

import pygame
pygame.init()

WIDTH = 700 
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Slime Jump")

bg = pygame.transform.scale(pygame.image.load('pygame files\Images\Moving Images HW Images\gb.jpg'), (WIDTH, HEIGHT))
slime1 = pygame.image.load('final_game\images\slimejumpimages\slime1.png')
slime2 = pygame.image.load('final_game\images\slimejumpimages\slime2.png')
slime3 = pygame.image.load('final_game\images\slimejumpimages\slime3.png')
slime4 = pygame.image.load('final_game\images\slimejumpimages\slime4.png')

platforms = [[270,550,150,10], [70, 450, 150, 10], [470, 450, 150, 10], [270,350,150,10],[70,250,150,10], [470,250,150,10]]
player_x = 225
player_y = 400
width = 40
height = 60
vel = 5
white = (255,255,255)
black = (0,0,0)
grey = (128,128,128)
jump = False
y_change = 0 
x_change = 0
player_speed = 3
left = False 
right = False
score = 0
high = 0

clock = pygame.time.Clock()

jump = False
jumpCount = 10

left = False
right = False
walkCount = 0

#changing images when going left or right
def redrawGameWindow():
    global walkCount
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:  
        screen.blit(slime3, (player_x,player_y))
        walkCount += 1                          
    elif right:
        screen.blit(slime2, (player_x,player_y))
        walkCount += 1
    else:
        screen.blit(slime1, (player_x,player_y))
        walkCount = 0
        
    pygame.display.update() 

#check for collision with blocks 
def check_collisions(rect_list, j):
    global player_x, player_y, y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([player_x, player_y+60, 90, 50]) and jump == False and y_change > 0: #checks is rect collides when jump == false and player is falling 
            j = True
    return j

#update user y positions every loop 
def update_player(y_pos):
    global jump, y_change
    jump_height = 10
    gravity = 0.5
    if jump: #send player jumping but then immidietly bring back down 
        y_change = -jump_height
        jump = False
    y_pos += y_change
    y_change += gravity #gravity affects immidietetly 
    return y_pos

#handle movement of platforms as game progresses 
def update_platforms(my_list, y_pos, change):
    global score
    if y_pos < 250 and change < 0: #only when you are jumping and hit position fo 250 will the screen go up
        for i in range(len(my_list)):
            my_list[i][1] -= change
    else:
        pass 
    for item in range(len(my_list)):
        if my_list[item][1] > 600:
            my_list[item] = [random.randint(50,520), random.randint(250,300), 150,10]
            score += 1
    return my_list


run = True
while run:
    clock.tick(27)
    blocks = []
    screen.fill(white)
    for i in range(len(platforms)):                                 # 0,5 makes it round and filled in 
        block = pygame.draw.rect(screen, black, platforms[i], 0,5) #[i] making length height cuardonates as platform []
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_x > vel:
                player_x -= vel
                left = True
                right = False
            if event.key  == pygame.K_RIGHT and player_x < 500 - vel - width:  
                player_x += vel
                left = False
                right = True
            else: 
                left = False
                right = False
                walkCount = 0
            if not(jump):
                if event.key == pygame.K_SPACE:
                    jump = True
                    left = False
                    right = False
                    walkCount = 0
            else:
                if jumpCount >= -10:
                    player_y -= (jumpCount * abs(jumpCount)) * 0.5
                    jumpCount -= 1
                else: 
                    jumpCount = 10
                    jump = False
    
    jump = check_collisions(blocks, jump)
    player_x += x_change

    if player_y <640:
        player_y = update_player(player_y) #use to control up and down movement 
    else:
        game_over = True
        y_change = 0

        
    platforms = update_platforms(platforms, player_y, y_change) #lets you know how much you need to modify loction fo platforms 
    
    if player_x < -70:
        player_x = -70 
    elif player_x > 550:
        player_x = 550

    if score > high:
        high = score 

    redrawGameWindow() 
    
pygame.quit()