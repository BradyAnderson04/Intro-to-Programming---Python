from turtle import *
import random as rn 
color('red')
# want to go a full circle - set variables to only go in one full circle

length = 30

def circleSnowflake():
    # reset degree of rotation on each new function call
    turn = rn.randint(20, 60) // 5
    repetitions = 360 // turn
    if(turn < 30):
        repetitions = repetitions / 2
    # draw whole thing
    for i in range(int(repetitions)):
        # draw one branch
        for i in range(5):
            forward(length)
            left(turn)
            forward(length)
            backward(length)
            right(2 * turn)
            forward(length)
            backward(length)
            left(turn)
        forward(length)
        backward(length * 6)
        if(turn < 30):
            left(turn * 2)
        else:
            left(turn)
    
def drawCircle(variance, yheight):
    penup()
    setpos(0, yheight)
    pendown()
    # draw a circle
    for i in range(360):
        forward(variance)
        left(1)
    penup()
    setpos(0, 0)
    pendown()
    



drawCircle(1.05, -60)
circleSnowflake()
drawCircle(2.1, -120)
done()