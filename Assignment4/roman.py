romanNumerals = {5: 'V', 10: 'X', 50: 'L', 100: 'C'}        # Special characters dict
numerals = []                                               # List to return
# Supporting Functions 
def prefix(num, i): 
    if(int(num) < 40):
        return (i * 'X')
    elif(int(num) < 50):
        return 'XL'
    elif(int(num) < 90):
        return ('L' + ((i -5) * 'X'))
    else:
        return 'XC'
def numeralRules(i, j):
    roman = ''
    if(j % 10 < 4):                     # j is 1 - 3
        roman = (prefix(num, i) + ('I' * j))
    elif(j % 10 == 4 or j % 10 == 9):   # j is 4 or 9
        roman = (prefix(num, i) +('I' + romanNumerals[(j+1)]))
    elif(j % 10 < 9 and j != 5):       # j is 6 - 8
        roman = (prefix(num, i) +('V' + ('I' * (j-5))))
    else:                               # j == 5
        roman = (prefix(num, i) + 'V')
    return roman
def appendValue(num, roman):
    item = num + ': ' + roman
    numerals.append(item)
for i in range(0, 10):              # list numbers from 1 to 99
    for j in range(0, 10):
        # create a value to check and include in print
        num = str(i) + str(j)
        # seperate by group of similar rules
        if(num != '00'):
            roman = numeralRules(i, j)
            appendValue(num, roman)
print(numerals)