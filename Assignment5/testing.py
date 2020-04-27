'''
Messing around w/ building a version of magic square function that will 
Tell if magic square or not regardless of square size

'''
ms = [[4, 9, 2],[3,5,7],[8,1,6]]
ms = [[1, 15, 14, 4], [10, 11, 8, 5], [7, 6, 9, 12], [16, 2, 3, 13]]

def checkRows(ms):
    total = 0
    status = False
    for i in range(len(ms)):
        calcSum = 0
        for j in range(len(ms)):
            if(i == 0):
                total += ms[i][j]
            else:
                calcSum += ms[i][j]
                if(calcSum == total):
                    status = True
                else:
                    status = False
    return status

def checkColumn(ms):
    total = 0
    status = False
    for i in range(len(ms)):    # goes through total amount of rows
        calcSum = 0
        column = 0
        while(column < len(ms[i])): # specific val in column
            print(ms[i][column])

            column += 1

print(checkRows(ms))
