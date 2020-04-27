import pygame, sys
import math
from pygame.locals import*
import random as rn
pygame.init()

BLUE = (0,0,255)
WHITE = (255,255,255)
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption('S-Triangle')

#INPUT takes a location loc = (x,y) pair of points and width
#RETURN 3 points of the equilateral triangle determined by loc and width
def triangle(loc,width):
    #TODO: Implement function
    z = math.sqrt(width ** 2 - ( width / 2) ** 2)
    # find top 
    x1 = loc[0] + width / 2
    y1 = loc[1]
    # find left
    x2 = loc[0]
    y2 = loc[1] + z
    # find right
    x3 = loc[0] + width
    y3 = loc[1] + z
    return ((x1, y1), (x2, y2), (x3, y3))

DISPLAYSURF.fill(WHITE)

#Draws Triangle
#(triangle(loc,w)) is a tuple of tuples...)
def draw_triangle(loc, w):
    pygame.draw.polygon(DISPLAYSURF, Color(rn.randint(0, 255),rn.randint(0, 255),rn.randint(0, 255)) , (triangle(loc,w)),1)

#INPUT location and width
#RETURN nothing -- follows algorithm
def s(loc,width):
    #TODO: Implement Function
    if(width > 1):
        z = math.sqrt(width ** 2 - ( width / 2) ** 2)
        draw_triangle(loc, width)
        s((loc[0] + width/ 4, loc[1]) , width/2)
        s((loc[0], loc[1] + z/2) , width/2)
        s((loc[0] + width/2, loc[1] + z/2) , width/2)
    else: 
        return
    

s((0,0),440)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()