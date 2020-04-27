'''
Check if this is an isogram

for the normies in the room...an isogram is something that doesn't have repeat letters

Can't use built in python functions
'''

def is_isogram(xword):
    #TODO complete function
    letterCount = {}
    status = True
    for i in range(len(xword)):
        print(xword[i])
        if(xword[i] in letterCount.keys()):
            status = False
            print('false')
        else:
            letterCount[xword[i]] = 1
    return status
    
if __name__=="__main__":
    words = ["dermatoglyphics","palindrome", "anagram"]
    
    for w in words:
        print(is_isogram(w))