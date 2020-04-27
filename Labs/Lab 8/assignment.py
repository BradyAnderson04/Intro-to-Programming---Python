### This lab assignment will be done in "Labs/Lab9/lab9.py"
import random as rn
### Generators
def roll(size):
    while True:
        r = rn.randint(1, size)
        yield r
        
def diceRolls(diceList):
    """
    Given a list of tuples, where each tuple is structured as:
    (size of dice, number of rolls)
    Where the "size of the dice" is rolled that many times in a row. 
    Each call to the generator produces a single value. 
    You will need to use a certain function from the 
    `random` module. 
    ---------------------------------------------------------------------------
    Example:
    >>> tuples = [(20, 4), (6, 3)]
    >>> print([i for i in diceRolls(tuples)])
    [13, 17, 18, 17, 5, 6, 1] 
    # Note that this will be a different list because of random
    """
    rollList = []
    for i in diceList:
        x1 = roll(i[0])
        rollList.append([next(x1) for j in range(i[1])])
    return rollList

    



### List Comprehension

"""
All list comprehensions must be written as one expression. 
While coding them, it is alright to test with multiple lines, 
but when finalizing your solution for a problem, condense it 
into one expression.
"""

def splitCharacters(word):
    """
    Given a single word, split up each character into it's own element within a list. 
    Extra challege, you cannot keep spaces (' ' (ignore quotes)).
    """
    return [i for i in word if ord(i) != 32]

def oddNumbers():
    """
    Return a list of all odd numbers less than 50
    """
    return [i for i in [i for i in range(55)] if (i % 2 == 1 and i < 50)]
    

def dictionaryProblem(d):
    """
    Given a dictionary, where each key is a string and a value is a number, 
    create a dictionary with all keys and their associated value that have a 
    value over 1
    sample dictionary
    {'a':2, 'b':1, 'c':4, 'd':10, 'e':1}
    """
    return { k:v for (k,v) in d.items() if v > 1}

### Memoized

def fibMemo(n):
    """
    Given the nth fibonacci number, calculate the value. 
    Do this with memoization (determine where to put the dictionary)
    Fib(0) = 0
    Fib(1) = 1
    Fib(2) = 1
    Fib(3) = 2
    ...
    Fib(11) = 89
    
    F(n) = F(n-1) + F(n - 2)
    """
    d = {0:0, 1:1}
    for i in range(2, n+1):
        if i in d.keys():
            return d[i]
        else:
            d[i] = d[i-1] + d[i-2]
    return d[n]
            


### Test code

if __name__ == "__main__":
    # Generators
    print('Dice Rolls:', diceRolls([(20, 4), (6, 3)]))
    # list comprehensions
    print('Split Characters:', splitCharacters('Hello world'))
    print('Odd Numbers:', oddNumbers())
    print('Dictionary Problem:', dictionaryProblem({'a':2, 'b':1, 'c':4, 'd':10, 'e':1}))
    # Memoization
    print('Fibonachi Sequence:', fibMemo(11))