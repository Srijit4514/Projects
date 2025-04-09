import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Example")

# Set up colors

BLCK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the square

square_size = 50
square_x = width // 2 - square_size // 2
square_y = height // 2 - square_size // 2
square_speed_x = 5
square_speed_y = 5

# Main game loop 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the square 
    square_x += square_speed_x
    square_y += square_speed_y

    # Bounce the square off the edges
    if square_x <= 0 or square_x >= width - square_size:
        square_speed_x = -square_speed_x
    if square_y <= 0 or square_y >= height - square_size:
        square_speed_y = -square_speed_y

    # Fill the screen with black
    screen.fill(BLCK)

    # Draw the square
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))

    # Update the disqlay
    pygame.display.flip()

    # Coltrol the fram rate
    pygame.time.Clock().tick(60)

