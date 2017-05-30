# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "PACMAN BY: CARRINGTON JONES"
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

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    #Ghost
    pygame.draw.rect(screen, ORANGE, [580, 220, 120, 40])
    pygame.draw.rect(screen, ORANGE, [540, 260, 200, 40])
    pygame.draw.rect(screen, ORANGE, [500, 300, 280, 240])
    pygame.draw.rect(screen, ORANGE, [500, 540, 40, 40])
    pygame.draw.rect(screen, ORANGE, [580, 540, 40, 40])
    pygame.draw.rect(screen, ORANGE, [660, 540, 40, 40])
    pygame.draw.rect(screen, ORANGE, [740, 540, 40, 40])
    pygame.draw.rect(screen, WHITE, [540, 340, 80, 80])
    pygame.draw.rect(screen, WHITE, [660, 340, 80, 80])
    pygame.draw.rect(screen, BLACK, [540, 380, 40, 40,])
    pygame.draw.rect(screen, BLACK, [660, 380, 40, 40])

    #Pacman
    pygame.draw.rect(screen, YELLOW, [440, 400, 40, 40])
    pygame.draw.rect(screen, YELLOW, [380, 400, 40, 40])
    pygame.draw.rect(screen, YELLOW, [320, 400, 40, 40])
    pygame.draw.rect(screen, YELLOW, [140, 280, 200, 20])
    pygame.draw.rect(screen, YELLOW, [120, 300, 260, 20])
    pygame.draw.rect(screen, YELLOW, [100, 320, 300, 40])
    pygame.draw.rect(screen, YELLOW, [80, 360, 280, 20])
    pygame.draw.rect(screen, YELLOW, [80, 380, 220, 20])
    pygame.draw.rect(screen, YELLOW, [60, 400, 200, 20])
    pygame.draw.rect(screen, YELLOW, [60, 420, 180, 20])
    pygame.draw.rect(screen, YELLOW, [60, 440, 200, 20])
    pygame.draw.rect(screen, YELLOW, [60, 460, 240, 20])
    pygame.draw.rect(screen, YELLOW, [60, 480, 300, 20])
    pygame.draw.rect(screen, YELLOW, [80, 500, 320, 40])
    pygame.draw.rect(screen, YELLOW, [100, 540, 280, 20])
    pygame.draw.rect(screen, YELLOW, [140, 560, 200, 20])

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
