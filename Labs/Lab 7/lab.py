# Recursion
'''
Python doesn't want to mess up stack with recursion....python limits this to 1000

Tail recursion does calculation in the call back
-Python this runs it faster but still creates a new stack
-Tail Recusion doesn't quite work in python interpreter....

Typically we don't want to use recursion unless required by the problem

'''

'''
Generators - Utilize yield

doesn't wait for whole function to run
calculates everything on the line sequentially

example below

Generators can generate infinite streams of data and stop when you want them to be stopped
'''

# def f():
#     i = 0
#     while True:
#         yield i
#         i += 1

# List comprehension examples
# generates terms and adds iterable

# sum can take any number of parameters
def sum(*args):
    total = 0
    if args:
        for i in args:
            if '__iter__' in dir(args[0])
                total += i
            
    else:
        return total

a = sum(1,2,3,4,5,6,7,8)
b = sum(*[1,2,3,4,5,6,7,8])

print(a)
print(b)
'''
s = sum(x * 3 for x in range(18) if x % 2 == 1)
print(s)



Comprehensions
    - reformating list comprehsnion to create different data structures
'''
# generates list and sums as one
l = sum(*[x * 3 for x in range(18) if x % 2 == 1])
print(l)

# checking if a data structure is iterable

print(dir([1,2,3,4,5]))
