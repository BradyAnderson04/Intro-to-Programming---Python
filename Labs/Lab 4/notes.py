# Loops - Bounded vs unbounded 
# Bounded Loop - Known amount of executions -> For
# Unbounded Loop - Unknown amount of executions -> While - more POWERFUL

# while True:
#    print('hello world. I run forever!')

#Syntax -> 
booleanExpression = True
cnt = 0
while booleanExpression:
    if cnt > 3:
        booleanExpression = False
    cnt +=1

# Runs sequentially    
a = True
while a:
    print('one')
    a = False
    print('two')

# Transfer for to while
'''
for i in range(5):
    print()

for i in container:
    print()
'''
# range function outline
# range(start, stop, step)

start = 0
stop = 5
step = 1

for i in range(start, stop, step):
    print(i)

i = start
while i < stop:
    print(i)
    i += step

# For loops are made for iterating through containers
container = ['a', 'b', 'c']
for i in container:
    print(i)

# you have to tell while loop to iterate
while container:
    print(container[0])
    container = container[1:]

# Container gets emptied because lists are mutable
print(container)

# container Structure
'''
container[start, stop, step]
ex:
container = container[::-1]
-> makes a reverse copy of list
'''


# Dictionary time

'''
Dictionaries are a pair of data
Every key must be unique 
only certain objects can be keys -> Immutable

Hashing -> An object is put into a function and you are returned a hash code

Same object gives same hash code -> so hashing is getting a different code for each key

Int, Strings, Bool, 

dictonaries and lists can't be keys
'''

dictionaryOne = {'a': [1,2,3,4], 'b': 28, 'c': 'hello world'}

#looping
#Value
for i in dictionaryOne:
    print(dictionaryOne[i])

# both
for k, v in dictionaryOne.items():
    print(k, v)

# adding a key
dictionaryOne['f'] = 2

# remove
print(dictionaryOne.pop('f'))