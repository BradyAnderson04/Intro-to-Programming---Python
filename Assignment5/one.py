def lr(xlst):
    # find the longest run of same data points
    maxCount = 0
    count = 0
    for j in range(len(xlst)):
        if(xlst[j] == 1 and (xlst[j-1]) == 0 or xlst[j] == 1 and (xlst[j-1]) == 1):
            count += 1
        elif(xlst[j] == 0 and count > maxCount):
            maxCount = count
            count = 0
        else:
            count = 0
    return maxCount
            



x = [0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0]
print(lr(x))

'''

'''