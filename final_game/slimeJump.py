#Christan Park
#slime jump game 

import pygame, os, random
pygame.init()
os.system('cls')

white = (255,255,255)
black = (0,0,0)
grey = (128,128,128)
WIDTH = 700 
HEIGHT = 600
fps = 60
MENU_FONT = pygame.font.SysFont('comicsans', 30)
clock = pygame.time.Clock()
score = 0
high = 0 
game_over = False

player_x = 225
player_y = 400
platforms = [[270,550,150,10], [70, 450, 150, 10], [470, 450, 150, 10], [270,350,150,10],[70,250,150,10], [470,250,150,10]]
jump = False
y_change = 0 
x_change = 0
player_speed = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Slime Jumper')

slime1 = pygame.image.load('final_game\images\slimejumpimages\slime1.png')
slime2 = pygame.image.load('final_game\images\slimejumpimages\slime2.png')
slime3 = pygame.image.load('final_game\images\slimejumpimages\slime3.png')
slime4 = pygame.image.load('final_game\images\slimejumpimages\slime4.png')

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
    if player_y < 250 and change < 0: #only when you are jumping and hit position fo 250 will the screen go up
        for i in range(len(my_list)):
            my_list[i][1] -= change
    else:
        pass 
    for item in range(len(my_list)):
        if my_list[item][1] > 600:
            my_list[item] = [random.randint(50,520), random.randint(250,300), 150,10]
            score += 1
    return my_list



Slime_Jump = True 
while Slime_Jump:
    clock.tick(fps)
    screen.fill(white)
    screen.blit(slime1,(player_x, player_y))
    blocks = []
    score_text = MENU_FONT.render('Score: '+ str(score), True, black, white)
    screen.blit(score_text, (530,20))
    highscore_text = MENU_FONT.render('High Score: '+ str(score), True, black, white)
    screen.blit(highscore_text, (490,60))

    for i in range(len(platforms)):                                 # 0,5 makes it round and filled in 
        block = pygame.draw.rect(screen, black, platforms[i], 0,5) #[i] making length height cuardonates as platform []
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Slime_Jump = False
            # mainMenu(title_main, message_menu, True)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -player_speed
            if event.key == pygame.K_RIGHT:
                x_change = player_speed
        if event.type == pygame.K_UP:
            if event.key == pygame.K_LEFT:
                x_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 0

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

    if x_change > 0:
        player = pygame.image.load('final_game\images\slimejumpimages\slime2.png')
    elif x_change < 0:
        player = pygame.transform.flip(pygame.image.load('final_game\images\slimejumpimages\slime3.png'), 1,0)

    if score > high:
        high = score 



    pygame.display.flip()
pygame.quit()