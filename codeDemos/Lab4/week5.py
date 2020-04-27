def occurencesWhile(lst, var):
    # count amount of var occurances
    cnt = 0
    i = 0
    while i < len(lst):
        if lst[i] == var:
            cnt+=1
        i += 1
    return cnt

def occurencesWhileList(lst, var):
    item = 0
    while lst:
        if lst[0] == var:
            item += 1
        lst.pop(item)
    return item

def operationList(opsList, opp):
    '''
    Given a list of lists 

    we will either s, m, a
    '''
    resultList=[]
    indexOne = 0
    indexTwo = 0
    while (indexOne < len(opsList)):
        while( indexTwo < len(opsList[indexOne])):
            if(opp == 'm'):
                result = 1
                result *= opsList[indexOne][indexTwo]
            elif(opp == 'a'):
                result = 0
                result += opsList[indexOne][indexTwo]
            elif(opp == 's'):
                result = 0
                result -= opsList[indexOne][indexTwo]
            indexTwo += 1
        indexOne += 1
        resultList += result
    return resultList

def evenCount2(dictionary):
    count = 0
    for key in dictionary:
        if key % 2 == 0:
            count += 1
        
    return count

