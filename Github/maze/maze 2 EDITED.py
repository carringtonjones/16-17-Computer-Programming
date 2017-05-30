import time


# Imports
import pygame
import intersects
import random

# Initialize game engine
pygame.init()

# Window
WIDTH = 1080
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)
TITLE = "ESCAPE ROUTE"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)
#Clock
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 255, 0)
BLUE = (0, 195, 195)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
LIME_GREEN = (200, 244, 66)
BRIGHT_GREEN = (176, 244, 66)
TURQOUISE = (66, 244, 143)
SEA_GREEN = (66, 244, 188)
ALMOSTFOREST_GREEN = (1, 79, 63)
PINK = (255, 38, 88)

#Images
img1 = pygame.image.load('images/START.png')

# Make a player
player =  [719, 1079, 3, 3]
player_vx = 0
player_vy = 0
player_speed = .5

#Define Screen boundary
wall1 =  [0, 0, 1080, 1]
wall2 = [1080, 0, 1, 720]
wall3 = [0, 0, 1, 720]
wall4 = [0, 720, 1080, 1]
boundary = [wall1, wall2, wall3, wall4]

# Fonts
MY_FONT = pygame.font.Font(None, 50)


# stages
START = 0
PLAYING = 1
END = 2


def setup():
    global stage, player, time_remaining, ticks
    stage = START
    player =  [1, 4, 3, 3]

    time_remaining = 40
    ticks = 5


blocks = []
for x in range (0, 1080, 25):
    for y in range (30, 720, 25):
        l = [x, y, 10, 10]
        blocks.append(l)            
for x in range (0, 1080, 25):
    for y in range (30, 720, 25):
        l = [x,y, 20, 3]
        blocks.append(l)
        c = [x, y, 5, 5]
coins = []
for x in range (100, 980, 5):
    for y in range (0, 700, 5):
        l = [x, y, 40, 40]


# Game loop
setup()
win = False
score = 0
done = False
while not done:

    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:
            
            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                  
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()


    if stage == PLAYING:
        pressed = pygame.key.get_pressed()
        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]
    
        if up:
            player_vy = -player_speed
        elif down:
            player_vy = player_speed
        else:
            player_vy = 0     
        if left:
            player_vx = -player_speed
        elif right:
            player_vx = player_speed
        else:
            player_vx = 0
            
      

    # Game logic
    if stage == PLAYING:
        ''' move block '''
        player[0] += player_vx

        ''' resolve collisions horizontally '''
        for b in boundary:
                if intersects.rect_rect(player, b):        
                    if player_vx > 0:
                        player[0] = b[0] - player[2]
                    elif player_vx < 0:
                        player[0] = b[0] + b[2]
        for l in blocks:
                if intersects.rect_rect(player, l):        
                    if player_vx > 0:
                        player[0] = l[0] - player[2]
                    elif player_vx < 0:
                        player[0] = l[0] + l[2]
        
        player[1] += player_vy
     
        ''' resolve collisions vertically '''
        for b in boundary:
            if intersects.rect_rect(player, b):                    
                if player_vy > 0:
                    player[1] = b[1] - player[3]
                if player_vy < 0:
                    player[1] = b[1] + b[3]
        for l in blocks:
            if intersects.rect_rect(player, l):                    
                if player_vy > 0:
                    player[1] = l[1] - player[3]
                if player_vy < 0:
                    player[1] = l[1] + l[3]
                    
    if stage == PLAYING:
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END
            
    # Drawing code
    screen.fill(ALMOSTFOREST_GREEN)
    pygame.draw.rect(screen, WHITE, player)
 
    #Timer Text
    timer_text = MY_FONT.render(str(time_remaining), True, WHITE)
    screen.blit(timer_text, [0, 0])

    #Draw The Walls
    for b in boundary:
        pygame.draw.rect(screen, BLACK, b)
    for l in blocks:
        pygame.draw.rect(screen, BLUE, l)
        
    ''' begin/end game text '''
    if stage == START:
        screen.blit(img1, (0,0))
        text1 = MY_FONT.render("", True, WHITE)
        screen.blit(text1, [350, 150])
     
    elif stage == END:
        text1 = MY_FONT.render("YOU DIDNT GET THERE IN TIME", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)


# Close window on quit
pygame.quit()
