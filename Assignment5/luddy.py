import numpy as np

valCost = {'x': 5, 'y': 10}

def costCalc(x, y):
    return valCost['x']*x + valCost['y']*2*y + valCost['y']*x

def area(x,y):
    # check if area is right area
    return x * y == 75

ax = 0
by = 0
def f(x,y):
    minCost = 100000000
    for i in np.arange(0, 100, .25):
        for j in np.arange(0, 100, .25):
            if(area(i, j) and costCalc(i, j) < minCost):
                minCost = costCalc(i,j)
                x = i
                y = j
    ax = x
    by = y
    print(ax)
    print(by)
    return minCost

#MARVELOUS BRUTE FORCE
print(ax,by, f(ax,by))