import random as rn

def twoMax(xlst):
    def mymax(x,y):
        if x >= y:
            return x
        else:
            return y
    # TODO: Finish the function
    max = []
    if(len(xlst) == 1 and bool(xlst[0])):
        return mymax(xlst[0][0], xlst[0][1])
    elif(len(xlst) > 1):
        max = mymax(mymax(xlst[0][0], xlst[0][1]), twoMax(xlst[1:]))
    return max
        

#TODO: IMPLEMENT RECURSIVE FUNCTION

if __name__=="__main__":
    testlst = rn.randint(0,10)
    lst = []
    while testlst:
        lst.append([rn.randint(0,20),rn.randint(0,20)])
        testlst -= 1
        
    print(lst)
    answer = twoMax(lst)
    print(answer)