def min(x,y):
    #TODO: Implement function
    if(x <= y):
        return x
    else:
        return y
    
def MIN(lst):
    #TODO: Implement function recursively
    if(len(lst) < 2):
        return min(lst[0], lst[0])
    else:
        return min(lst[0], MIN(lst[1:]))

# for-loop and index into list
def min1(x):
    #TODO: Implement function
    minimum = 10000
    for i in range(len(x)):
        if(x[i] < minimum):
            minimum = x[i]
    return minimum
    
# for-loop and container
def min2(x):
    #TODO: Implement function
    minimum = 10000
    for i in x:
        if(i < minimum):
            minimum = i
    return minimum
    
# while-loop and index into list
def min3(x):
    #TODO: Implement function
    xlst = x[:]
    while len(xlst) > 1:
        if(xlst[0] <= xlst[1]):
            xlst.remove(xlst[1])
        else:
            xlst.remove(xlst[0])
    return xlst[0]
            
    
# while-loop and container
def min4(x):
    #TODO: Implement function
    xlst = x[:]
    minimum = 10000
    while xlst:
        if(xlst[0] <= minimum):
            minimum = xlst[0]
        xlst=xlst[1:]
    return minimum

# for loop reverse index    
def min5(x):
    small = x[-1]
    for i in range(len(x)-1,-1,-1):
        if x[i] < small:
            small = x[i]
    return small

if __name__=="__main__":
    x = [1,42,-1,22,0,12]  
    mf = [MIN, min1, min2, min3, min4, min5]
    for f in mf:
        print("{0}({1}) = {2}".format(f.__name__,x,f(x)))