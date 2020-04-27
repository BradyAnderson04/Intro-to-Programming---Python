# Module imports
import pygame
import sys
import math

max_iterations = 30

i = 0
def mandlebrot(c):              # (z , c)
    # calculate z 
    if(abs(z) > 2 or i == 30):      # base case
        z = z*z + c
        i += 1
        return mandlebrot(c, z, i)
    else:           # recursion
        return i

pygame.init()

# Colors
BLACK = (0,0,0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Pygame stuff
size = [300, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Mandlebrot Problem')
screen.fill(WHITE)

# Create array of pixels
pixAr = pygame.PixelArray(screen)

for x in range(-150, 150):
    for y in range(-150, 150):
        c = (x/150, y/150)
        v = mandlebrot(c, 0, 0)
        if(v < max_iterations):
            pixAr[x + 150, y + 150] = RED
        else:
            pixAr[x + 150, y + 150] = BLACK

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


# Testing
print('Max Iterations = {0}'.format(max_iterations))
for a in range(-10, 10, 5):
    for b in range(-10, 10, 5):
        c = complex(a/10, b/10)
        print(c, mandlebrot(c))