# Computer Programming 1
# Unit 11 - Graphics
#
# Track ticks to draw different animation frames.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
BLACK = (0, 0, 0)

RED = (255, 0, 0)
ORANGE = (255, 125, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (255, 0, 255)


def draw_person(screen, x, y, frame):
    if frame == 0:
        pass

    elif frame == 1:
        pass

    elif frame == 2:
        pass

    
    
# Game loop
done = False
ticks = 0

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    frame = ticks // 10
    
    ticks += 1

    if ticks >= 60:
        ticks = 0
        
    # Drawing code
    screen.fill(BLACK)

    if frame == 0:
        pygame.draw.rect(screen, RED, [350, 250, 100, 100])
    elif frame == 1:
        pygame.draw.rect(screen, ORANGE, [350, 250, 100, 100])
    elif frame == 2:
        pygame.draw.rect(screen, YELLOW, [350, 250, 100, 100])
    elif frame == 3:
        pygame.draw.rect(screen, GREEN, [350, 250, 100, 100])
    elif frame == 4:
        pygame.draw.rect(screen, BLUE, [350, 250, 100, 100])
    elif frame == 5:
        pygame.draw.rect(screen, VIOLET, [350, 250, 100, 100])
        

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
