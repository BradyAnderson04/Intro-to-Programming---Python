# memoization
# d = {}
'''
def fun(n):
    # make sure to check if exists in dict already!
    d[n] = whatever we want
    return d[n]

'''

# better method - closure
# def fun(n):
#     d={}
#     def wrapped(n, count):
#         # insert memoization here!
#         return
#     return wrapped(n, 0)

# syntax for list compreshensions
'''
1.Select - is the output
2.from - the source of data
3.where - predicate that holds the data
'''
# [0 for i in a for k in b]

'''
Avoid hacky solutions

'''

# dictionary comprehensions
a = 'message'
d = {letter : 10 for letter in a}
print(d)

# string = '0123456789abcdef'
# print(string.hexdigits)
# hexd = {i:j for i, j in zip(string.hexdigits, range(16))}
# print(hexd)

cont = '0123456789abcdef'
for n, l in enumerate(cont):
    print(n,l)

def matrx(row, colums, defaultValue):
    return [[defaultValue for c in range(columns)] for r in range(rows)]

# Assignment for lab