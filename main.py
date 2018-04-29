# LaunchDraw
# By: Evan Pratten (ewpratten)
# http://retrylife.ca
# Thanks to http://programarcadegames.com for example code

import launch
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each buttons location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5

# Build array
buttons = []
for row in range(9):
    # Add an empty array that will hold each cell
    # in this row
    buttons.append([])
    for column in range(9):
        buttons[row].append(False)  # Append a cell

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [230, 230]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("LaunchDraw")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to buttons coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            buttons[row][column] = not buttons[row][column]
            launch.setlight(column, row)


    screen.fill(BLACK) # black BG

    for row in range(9):
        for column in range(9):
            color = WHITE
            if buttons[row][column] == True:
                color = GREEN
            pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
launch.flush()