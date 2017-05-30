# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
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

# Make a player
player =  [600, 240, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 3

# make walls
wall1 =  [0, 0, 25, 240]
wall2 =  [0, 0, 800, 25]
wall3 = [660, 0, 25, 100]
wall4 = [120, 0, 25, 480]
wall5 = [775, 0, 25, 240]
wall6 = [775, 360, 25, 240]
wall7 = [0, 575, 800, 25]
wall8 = [0, 360, 25, 240]
wall9 = [200, 180, 340, 25]
wall10 = [180, 180, 25, 300]
wall11 = [200, 260, 180, 25]
wall12 = [580, 0, 25, 160]
wall13 = [580, 160, 100, 25]
wall14 = [680, 140, 25, 45]
wall15 = [180, 20, 360, 25]
wall16 = [180, 40, 25, 60]
wall17 = [180, 100, 60, 25]
wall18 = [460, 200, 25, 80]
wall19 = [500, 420, 25, 180]
wall20 = [300, 100, 240, 25]
wall21 = [500, 420, 200, 25]
wall22 = [560, 340, 25, 80]
wall23 = [440, 340, 120, 25]
wall24 = [300, 320, 25, 200]
wall25 = [240, 495, 60, 25]
walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25]

# Make coins
coin1 = [210, 70, 25, 25]
coin2 = [240, 220, 25, 25]
coin3 = [400, 420, 25, 25]
coin4 = [720, 520, 25, 25]
coin5 = [620, 120, 25, 25]

coins = [coin1, coin2, coin3, coin4, coin5]


# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

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
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player[0] += player_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player, w):        
            if player_vx > 0:
                player[0] = w[0] - player[2]
            elif player_vx < 0:
                player[0] = w[0] + w[2]


    ''' move the player in vertical direction '''
    player[1] += player_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player, w):                    
            if player_vy > 0:
                player[1] = w[1] - player[3]
            if player_vy < 0:
                player[1] = w[1] + w[3]

    coins = [c for c in coins if not intersects.rect_rect(player, c)]

    if len(coins) == 0:
        win = True

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(TURQOUISE)

    pygame.draw.rect(screen, PINK, player)
    
    for w in walls:
        pygame.draw.rect(screen, BRIGHT_GREEN, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You're a WINNER!", 1, GREEN)
        screen.blit(text, [400, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
