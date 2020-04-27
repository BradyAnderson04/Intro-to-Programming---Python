def sumListFor(aList):
    sum = 0
    for i in aList:
        # If adding by 1 then it would make the length of the list
        # += long for is = x + var
        sum += i
    return sum

def neverGonna(listOfWrongDoings):
    """
    print Never gonna + ....
    """
    for doing in listOfWrongDoings:
        print('never gonna', doing)

def multiplyForLoop(aListing):
    """
    multiply the number in a list together using a for loop
    
    *= new technology!
    """
    product = 1
    for num in aListing:
        product *= num
    return product
