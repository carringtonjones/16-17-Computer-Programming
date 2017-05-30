# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (1200, 900)
TITLE = "UNCONTROLLABLE PACMAN BY: CARRINGTON JONES" 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
''' add colors you use as RGB values here '''
YELLOW = (244, 238, 66)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
PURPLE = (197, 66, 244) 
VIOLET = (216, 0, 57)
RED = (237, 0, 0)

def draw_pacman(screen, x, y):
    pygame.draw.rect(screen, YELLOW, [x + 320, y + 120, 40, 40])
    pygame.draw.rect(screen, YELLOW, [x + 260, y + 120, 40, 40])
    pygame.draw.rect(screen, YELLOW, [x + 380, y + 120, 40, 40])
    pygame.draw.rect(screen, YELLOW, [x + 80, y, 200, 20])
    pygame.draw.rect(screen, YELLOW, [x + 60, y + 20, 260, 20])
    pygame.draw.rect(screen, YELLOW, [x + 40, y + 40, 300, 40])
    pygame.draw.rect(screen, YELLOW, [x + 20, y + 80, 280, 20])
    pygame.draw.rect(screen, YELLOW, [x + 20, y + 100, 220, 20])
    pygame.draw.rect(screen, YELLOW, [x, y + 120, 200, 20])
    pygame.draw.rect(screen, YELLOW, [x, y + 140, 180, 20])
    pygame.draw.rect(screen, YELLOW, [x, y + 160, 200, 20])
    pygame.draw.rect(screen, YELLOW, [x, y + 180, 240, 20])
    pygame.draw.rect(screen, YELLOW, [x, y + 200, 300, 20])
    pygame.draw.rect(screen, YELLOW, [x + 20, y + 220, 320, 40])
    pygame.draw.rect(screen, YELLOW, [x + 40, y + 260, 280, 20])
    pygame.draw.rect(screen, YELLOW, [x + 80, y + 280, 200, 20]) 

    
def draw_ghost(screen, x, y, color):
    pygame.draw.rect(screen, color, [x + 80, y, 120, 40])
    pygame.draw.rect(screen, color, [x + 40, y + 40, 200, 40])
    pygame.draw.rect(screen, color, [x, y + 80, 280, 240])
    pygame.draw.rect(screen, color, [x, y + 320, 40, 40])
    pygame.draw.rect(screen, color, [x + 80, y + 320, 40, 40])
    pygame.draw.rect(screen, color, [x + 160, y + 320, 40, 40])
    pygame.draw.rect(screen, color, [x + 240, y + 320, 40, 40])
    pygame.draw.rect(screen, WHITE, [x + 40, y + 120, 80, 79])
    pygame.draw.rect(screen, WHITE, [x + 160, y + 120, 80, 80])
    pygame.draw.rect(screen, BLACK, [x + 40, y + 160, 40, 40,])
    pygame.draw.rect(screen, BLACK, [x + 160, y + 160, 40, 40])


def draw_dots(screen, x, y): 
    pygame.draw.rect(screen, YELLOW, [x + 320, y + 120, 40, 40])
    pygame.draw.rect(screen, YELLOW, [x + 260, y + 120, 40, 40])
    pygame.draw.rect(screen, YELLOW, [x + 380, y + 120, 40, 40])
    
# Game loop
done = False


red_ghost_x = 500
red_ghost_y = 220
orange_ghost_x = 800
orange_ghost_y = 220
yellow_pacman_x = 100 
yellow_pacman_y = 300

ghost_speed = 3
pacman_speed = 20

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    state = pygame.key.get_pressed()

    pm_up = state[pygame.K_UP]
    pm_down = state[pygame.K_DOWN]
    pm_left = state[pygame.K_LEFT]
    pm_right = state[pygame.K_RIGHT]

    red_up = state[pygame.K_a]
    red_down = state[pygame.K_b]
    red_left = state[pygame.K_c]
    red_right = state[pygame.K_d]

    orange_up = state[pygame.K_1]
    orange_down = state[pygame.K_2]
    orange_left = state[pygame.K_3]
    orange_right = state[pygame.K_4]
    

    # Game logic (Check for collisions, update points, etc.)

    if red_up:
        red_ghost_y -= ghost_speed

    if red_down:
        red_ghost_y += ghost_speed

    if red_left: 
        red_ghost_x -= ghost_speed

    if red_right:
        red_ghost_x += ghost_speed

    if orange_up:
        orange_ghost_y -= ghost_speed

    if orange_down:
        orange_ghost_y += ghost_speed

    if orange_left: 
        orange_ghost_x -= ghost_speed

    if orange_right:
        orange_ghost_x += ghost_speed

    if pm_up:
        yellow_pacman_y -= pacman_speed

    if pm_down:
        yellow_pacman_y += pacman_speed

    if pm_left: 
        yellow_pacman_x -= pacman_speed
        
    if pm_right:
        yellow_pacman_x += pacman_speed



    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    #Ghost
    draw_ghost(screen, red_ghost_x, red_ghost_y, RED)
    draw_ghost(screen, orange_ghost_x, orange_ghost_y, ORANGE)

    #Pacman
    draw_pacman(screen, yellow_pacman_x, yellow_pacman_y)
    

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
