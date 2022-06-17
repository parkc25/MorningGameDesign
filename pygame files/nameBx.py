#Christan Park
#6/17/2022
#get user name in pygame
import pygame, sys, os, random

pygame.init()
os.system('cls')

clock = pygame.time.Clock()

WIDTH = 600
HEIGHT = 600
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
backgrnd = (255,255,255)
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
menu_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255)) #random color generator
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(menu_color)
run = True 
user_name = ''
nameClr = (0,105,105)
bxClr = (200,200,200)

title = TITLE_FONT.render("Enter name ", 1, bxClr)
screen.blit(title, (WIDTH//2-100,200))
pygame.time.delay(500)

pygame.display.update()

name_box = pygame.Rect(WIDTH/2-90, HEIGHT//2, 200, 50)
while run:
     for event in pygame.event.get():
            if event.type==pygame.QUIT: #if press x go back to menu
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                #make box 
                name_box = pygame.Rect(WIDTH/2-90, HEIGHT//2, 200, 50)
                pygame.draw.rect(screen, colors.get("white"), name_box)
                pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_BACKSPACE:
                   user_name = user_name[:-1]
                else:
                    user_name+= event.unicode
            pygame.draw.rect(screen, bxClr, name_box)

            text_surface = MENU_FONT.render(user_name, True, nameClr)
            #user ur rect x, y, to 
            screen.blit(text_surface, (name_box.x+5, name_box.y+5))

            pygame.display.flip()

            #clock.tick(60) means that for every second at most  60 frams should be passed
            clock.tick(60)