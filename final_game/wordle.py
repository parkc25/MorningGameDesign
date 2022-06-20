#Christan Park 
# worlde game 

import pygame, sys, os, random
pygame.init()
os.system('cls')

#colors 
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), "grey":(96,96,96), "black":(0,0,0), "red":(255,0,0), "green":(0,255,0), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}

#screen/display
colors = ()
WIDTH = 700
HEIGHT = 700
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Wordle")
white = (255,255,255)
black = (0,0,0) #change to menu_color later 
green = (0,255,0)
yellow = (255,255,0)

#frame rate 
fpr = 60 
timer = pygame.time.Clock()

#board
board = [[" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],]

#other variables
turn = 0
LETTER_FONT = pygame.font.SysFont('comicsans', 55)
letters = 0
turn_now = True
game_over = False

#words for game 
# words = ("apple, power,  ")
# random_word = words[random.randint(0, len(words) - 1)]
random_word = "power"


def draw_board():
    global turn , board
    for col in range (0,5):
        for row in range(0,6):
            pygame.draw.rect(screen, black, [col*110+70, row*110+25, 90, 90], 4,5)
            letter_font = LETTER_FONT.render(board[row][col], True, black)
            screen.blit(letter_font, (col*110+80, row*110+35))
        pygame.draw.rect(screen, yellow, [5, turn*110+20, WIDTH-30, 100], 3, 5)


def check_word():
    global turn, board, random_word
    for col in range(0,5):
        for row in range(0,6):
            if random_word[col] == board[row][col] and turn > row:
                pygame.draw.rect(screen, green, [col*110+70, row*110+25, 90, 90], 0,5)
            elif board[row][col] in random_word and turn > row:
                pygame.draw.rect(screen, yellow, [col*110+70, row*110+25, 90, 90], 0,5)

running = True 
while running:
    timer.tick(fpr)
    screen.fill(white)
    check_word()
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.TEXTINPUT and turn_now and not game_over:
            guess = event.__getattribute__('text')
            board[turn][letters] = guess
            letters += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and letters > 0:
                board[turn][letters-1] = ' '
                letters -= 1 
            if event.key == pygame.K_SPACE:
                turn += 1 
                letters = 0 
            if event.key == pygame.K_RETURN:
                turn =0
                letters = 0 
                game_over = False
                # random_word = words[random.randint(0, len(words) -1 )]
                board = [[" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " "],]

    for row in range(0,6):
        guess = board[row][0] + board[row][1] +board[row][2] +board[row][3] +board[row][4]
        if guess == random_word and row < turn:
            game_over = True

        if letters == 5:
            turn_now = False
        if letters < 5:
            turn_now = True

        if turn == 6:
            game_over = True
            screen.fill(white)
            lose_text = LETTER_FONT.render("You lost", True, black)
            screen.blit(lose_text, (WIDTH//2 -100,HEIGHT//2-150))

        if game_over and turn < 6:
            screen.fill(white)
            win_text = LETTER_FONT.render("You Win!", True, black)
            screen.blit(win_text, (WIDTH//2 -100,HEIGHT//2-150))

    pygame.display.flip()
pygame.quit()
    


