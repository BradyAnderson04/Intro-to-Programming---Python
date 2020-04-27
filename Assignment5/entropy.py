import math
def characterCount(lst, character):
    count = 0
    for i in range(len(lst)):
        if(character == lst[i]):
            count += 1
    return (count / len(lst))
def makeProbability(xlst):
    probVals = {}
    for i in range(len(xlst)):
        probVals[xlst[i]] = characterCount(xlst, xlst[i])
    return probVals
def entropy(xlst):
    ent = 0
    for i in xlst:
        ent += ( xlst[i] * math.log(xlst[i],2))
    return -1 * ent

s1 = ['a','b','a','b','a','b','b','b']
s2 = [(1),(2),(3),(4)]
s3 = [1]
s4 = [1,2]
xlst = [s1,s2,s3,s4]
for i in xlst:
    print(entropy(makeProbability(i)))