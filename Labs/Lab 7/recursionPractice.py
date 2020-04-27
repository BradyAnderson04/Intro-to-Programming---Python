def length(cont):
    '''
    recursively returns the length of the cont
    '''
    if not cont:
        return 0
    else:
        return 1 + length(cont[1:])
    pass

def removePos(x, cont):
    '''
    recursively removes item from list cont that is at x
    return a list of all items from cont that are not were not at the x position

    ex removePost(1, ['a', 'b', 'c']) --> ['a', 'c']
    '''
    if not cont:
        # if match index stop when index matches
        return []
    else:
        # keep going if index does match
        if x:
            return [cont[0]] + removePos(x-1, cont[1:])
        else:
            return [] + removePos(x-1, cont[1:])
    

def sum2Dlist(mat):
    '''
    recursively go through and sum all the values from each row and add the result of
    each row together to get a final value
    ex
        [[1,2,3]
        [4,5,6]
        [7,8,9]] --> 45
    returns an integer
    '''
    if not mat:
        return 0
    else:
        # add the first row up + row and get rid of row just added
        return sum(x for x in mat[0]) + sum2Dlist(mat[1:])

print(length([1,2,3,4,5,6,7,8]))
print(removePos(2,['a', 'b', 'c', 'd', 'e']))
print(sum2Dlist([[1,2,3],[4,5,6],[7,8,9]]))