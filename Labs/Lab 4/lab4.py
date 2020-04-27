# Lab 4
# Fall 2019 C200 / H200
import random as r
import math
"""
Below, finish the dictionary. Each key is a side of a die (1 - 6), and the 
value is the opposite side of the die. The opposite side of a 
dice always adds up to 7
"""
dice_dict = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}


def twisted_die_roll():
    """
    Function that generates a random roll 1 - 6, and 
    uses previously defined dictionary to return the opposite side.

    If 1 was generated, return 6. 

    To understand Random, take a moment to read through the link to find what specific 
    function from the MODULE `random`.
    https://docs.python.org/3/library/random.html
    """
    # generate random num
    randomNumber = r.randint(1,6)
    #select opposite
    oppositeNumber = dice_dict[randomNumber]
    # return opposite
    return oppositeNumber

def twisted_dice_rolls(n):
    """
    Function that uses a for loop to generate `n` twisted die rolls. 
    (You must use a previous function you made) and store them in a 
    list. Return the list

    for 
    """
    #store n rolls in list
    nRolls = []
    # generate n rolls
    for roll in range(n):
        # utilize previoys function
        nRolls += [twisted_die_roll()]
    return nRolls
        

def stats_twisted_rolls_list(n):
    """
    Generate `n` twisted die rolls (either a for loop or using a previous function) and 
    determine the roll statitics (how many times a 1, 2, ... 6 was rolled) in a list. 
    Print the list AND return the list. 

    Hint: how can we keep track of the statistics since we only have an ordered list and 
    what ever number we just rolled
    """
    # Generate n rolls as a list of length n 
    rolls = twisted_dice_rolls(n)
    # initialize variables and list
    countList = [0,0,0,0,0,0]
    # Process list and add stats accordingly
    for roll in range(n):
        countList[rolls[roll]-1] += 1
    # Init final list
    # return stat list
    return countList

def stats_twisted_rolls_dictionary(n):
    """
    Generate `n` twisted die rolls (either a for loop or using a previous function) and determine
    the roll statistics (how many times a 1, 2, ... 6 was rolled) in a DICTIONARY. 
    Print the dictionary AND return the dictionary. 

    You cannot call `stats_twisted_rolls_list` in this function. 
    """
    # Init Rolls list
    rolls = twisted_dice_rolls(n)
    # Init dict
    rollDict ={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

    # generate rolls and add stats
    for roll in rolls:
        rollDict[roll] += 1

    # return dictionary
    return rollDict


def sumOfOddNumbers(listOfNums):
    """
    Using a while loop, find the odd numbers and add them up.
    """
    #Init var
    i = 0
    # Init List
    sum = 0
    # setup loop 
    while(i < len(listOfNums)):
        # remove even numbers
        if(listOfNums[i] % 2 == 1):
            sum += listOfNums[i]
        i += 1
    return sum

def getFirstHalfOfString(string):
    """
    Using a loop, get the characters from the first half of the string

    Note: You can't use slicing, you can use indexing
    """
    stop = math.ceil(len(string) / 2)
    return string[0:stop]

def getSecondHalfOfString(string):
    """
    Get the second half of the string.

    You must only use slicing (plus a couple of other functions) to get the
    second half of the string
    """
    start = math.ceil(len(string) / 2)
    return string[start:]


def main():
    """
    TODO: Fill in tests for each of the above functions.
    """
    ### Fill in tests for dice roll
    print(twisted_die_roll())
    print(twisted_dice_rolls(4))
    print(stats_twisted_rolls_list(200))
    print(stats_twisted_rolls_dictionary(10000))
    print(sumOfOddNumbers([1, 3, 4, 8, 10, 12, 3, 5]))
    print(getFirstHalfOfString('Hello World'))
    print(getSecondHalfOfString('Hello World'))
    ### Fill in tests for remaining functions
    # TODO




if __name__ == "__main__":
    main()