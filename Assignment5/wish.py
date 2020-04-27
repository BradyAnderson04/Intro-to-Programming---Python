# Helper Functions
def rowCheck(ms, ev):
    status = True
    for i in range(len(ms)):
        status = ms[i][0]+ms[i][1]+ms[i][2] == ev 
    return status

def checkColumn(ms, ev):
    status = True
    for i in range(len(ms)):
        status = ms[0][i]+ms[1][i]+ms[2][i] == ev
    return status

def checkDiagonals(ms, ev):
    return ms[0][0]+ms[1][1]+ms[2][2] == ev and ms[0][2]+ms[1][1]+ms[2][0] == ev

# Real Function
def is_magic(ms):
    ev = ms[0][0]+ms[0][1]+ms[0][2]
    if(checkDiagonals(ms, ev) and checkColumn(ms, ev) and rowCheck(ms, ev)):
        return 'Magic Square...you\'re icy'                 # Logic Reference
    else:
        return 'Not a magic square, but a muggle square'    # harry potter reference
ms = [[4, 9, 2],[3,5,7],[8,1,6]]

print(is_magic(ms))

ms = [[4, 9, 2],[3,5,7],[8,2,6]]

print(is_magic(ms))