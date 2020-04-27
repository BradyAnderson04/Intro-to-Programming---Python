import math
# Task 1: Finish the following four functions

def maxThree(x, y, z):
    if x > y and x > z:
        return x
    if y > x and y > z:
        return y
    if z > y and z > x:
        return z
    """
    Returns the maximum of the three parameters
    """
    # TODO implement this function


def minThree(p1, p2, p3):
    # if x < y and x < z:
    #     return x
    # if y < x and y < z:
    #     return y
    # if z < y and z < x:
    #     return z
    
    nums = sorted([p1, p2, p3])
    print(nums[0])
    return nums[0]
    """
    Returns the minimum of the three parameters
    """
    # TODO implement this function


def maxTwoSum(tomato, potato, idaho):
    nums = sorted([tomato, potato, idaho])
    return nums[1] + nums[2]
    """
    Returns the sum of the largest two parameters
    """
    # TODO implement this function


def minTwoSum(x, y, z):
    nums = sorted([x, y, z])
    return nums[0] + nums[1]
    """
    Returns the sum of the smallest two values
    """
    # TODO implement this function



# Task 2: Writing more functions

def circleArea(d):
    print('Diameter: ', d)
    r = d / 2
    return math.pi * r**2
    """
    Implement the code in the circle.py listing from Problem 2 of Assignment 1 
    as a function named circleArea that takes in the diameter of a circle and returns the area
    """
    # TODO implement this function


def areaDifference_rect(l1, w1, l2, w2):
    areaOne = l1 * w1
    areaTwo = l2 * w2
    return abs(areaOne - areaTwo)
    """
    This function takes in the lengths and widths of two different rectangles
    and returns the difference between their two areas
    """
    # TODO implement this function


def areaDifference_circle(d1, d2):
    r1, r2 = d1/2, d2/2
    areaOne, areaTwo = math.pi * r1**2, math.pi * r2**2
    return abs(areaTwo - areaOne)
    """
    This function takes in the diameters of two circles and returns    the difference
    between their two areas. Hint: this function can make use of the circleArea function
    """
    # TODO implement this function


# if name == "main":
#     pass

print(areaDifference_circle(2, 3))