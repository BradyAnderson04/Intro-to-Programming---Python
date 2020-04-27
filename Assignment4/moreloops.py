# Input Parameter: a list of, possibly empty, numbers x
# Returns: the max number in list x (does not have to be unique)
def maxFor(xlst):
    if xlst:
        max = 0
        for i in range(len(xlst)):
            if(xlst[i] > max):
                max = xlst[i]
        return max
    else:
        return None
 
# Input Parameter: a list of, possibly empty, numbers x
# Returns: the max number in list x (does not have to be unique)
def maxWhile(xlst):
    if xlst:
        cnt = 0
        max = 0
        while(cnt < len(xlst)):
            if(xlst[cnt] > max):
                max = xlst[cnt]
            cnt += 1
        return max
    else:
        return None
    
# Input Parameter: a non-empty list of numbers x
# Returns: the minimal number value in list x (does not have to be unique)
def minFor(xlst):
    if xlst:
        min = 500
        for i in range(len(xlst)):
            if(xlst[i] < min):
                min = xlst[i]
        return min
    else:
        return None

#Input Parameters:a list of numbers lst
#Returns: the list lst with all occurrences of evens removed
def RemoveEvens(xlst):
    newList = xlst[:]
    for i in newList:
        if(i % 2 == 0):
            newList.remove(i)   
    return newList

# Input Parameters: list that contains either integers or strings
# Return Value: oldX replaced with num copies newX
def myReplace(oldX, num, newX, xlst):
    newList = xlst[:]
    duplicateList = []
    for i in range(len(newList)):
        if(newList[i] == oldX):
            duplicateList.append(newX)
            duplicateList.append(newX)
        else:
            duplicateList.append(newList[i])
    return duplicateList

# Input Parameters: list of numbers
# Returns: sum of the odd numbers
# if there are no odd numbers, then print zero
# if the list is empty, print the empty list
def sumOdd(xlst):
    copy = xlst[:]
    sum = 0
    for i in range(len(copy)):
        if(copy[i] % 2 == 1):
            sum += copy[i]
    return sum

# Input Parameter: a list x of objects [x1, x2, x3,..., xn]
# Returns: a string that is the concatenation of all the strings
# in the list in order encountered
def StringConcat(xlst):
    bigString = ''
    copy = xlst[:]
    for i in range(len(copy)):
        if(type(copy[i]) == str):
            bigString = bigString + copy[i]
    return bigString

# Data
w = []
x = [1,42,24,22,61,100,0,42]
y = [2]
z = [555,333,222]
nlst = [w,x,y,z]
c = [0,1,1,0,1,4]
a = ["a","b","b", "a", "c","b","e"]
b = [1,1,2,1,1,2,1,1,2,1,3,1]
d = ["a","row","d","ef",]

print("maxFor_____")
for i in nlst:
    print(maxFor(i))
print("\nmaxWhile_____")
for i in nlst:
    print(maxWhile(i))
print("\nminFor_____")
for i in nlst:
    print(minFor(i))
print("\nRemoveEvens_____")
print(RemoveEvens(b))
print(RemoveEvens(c))
print("\nmyReplace_____")
print(myReplace(1,2,"dog",c))
print(myReplace(1,2,1,b))
print("\nsumOdd_____")
for i in nlst:
    print(sumOdd(i))
print("\nStringConcat_____")
print(StringConcat(a))
print(StringConcat(d))


if __name__ == "__main__":
    pass