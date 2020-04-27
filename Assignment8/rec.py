#TIMER FUNCTION -- deprecated in 3.8 FYI
#so you might get messages -- you can ignore them for now
import time

def ftimer(f,args):
    time_start = time.clock()
    f(args)
    time_elapsed2 = (time.clock()-time_start)
    return time_elapsed2

#1
def even(x):
    return x % 2 == 0

#2
def odd(x):
    return x % 2 == 1

#3
#Recursive
#INPUT n
#OUTPUT RE value
def b(n):
    if n < 3:
        return 0
    else:
        if even(n):
            return n - 1 + b(n-1)
        else:
            return n**2 + 1 + b(n-1)


#4
#TAIL RECURSIVE FOR 3
def btr(n,s):
    if n < 3:
        return s
    else:
        if even(n):
            return btr(n-1, s + n - 1 )
        else:
            return btr(n-1, s + n**2 + 1 )

#5 
#MEMOIZATION - I use a top down approach
#USE THIS DICTIONARY
d = {2:0,1:0}
def bm(n):
    if n in d.keys():
        return d[n]
    else:
        if even(n):
            d[n] = n - 1 + d[n-1]
            return d[n]
        if odd(n):
            d[n] = n**2 + 1 + d[n-1]
            return d[n]


for i in range(1,10): 
    print("f({0}) = {1}, {2}, {3}".format(i, b(i),btr(i,0),bm(i)))

fblist = [b(10), lambda i: btr(i,0), bm(3) ]
tlist = [round(ftimer(f,700)*10**5,2) for f in fblist]
print(tlist)
print()
###################################################

#7
#RECURSIVE IMPLMENTATION
#INPUT N
#OUTPUT RE VALUE
def gg(n):
    if (n==0):
        return 0
    else:
        return 1 + 2 * gg(n-1)

#8
#TAIL RECURSIVE
def gtr(n,s):
    if (n == 0):
        return s
    elif(n == 1):
        return s + 1
    else: # something wrong w/ my tail recursion
        return gtr(n-1, 2 * (s + 1))

#9
#MEMOIZATION DICTIONARY INSIDE
d = {0:0}
def gm(n):
    if n in d.keys():
        return d[n]
    else: 
        d[n] = 1 + 2 * d[n-1]
        return d[n]


fglist = [gg(10), lambda i: gtr(i,0),gm(3)]

for i in range(0,10):
    print("f({0}) = {1}, {2}, {3}".format(i,gg(i),gtr(i,0),gm(i)))
    

tlist = [round(ftimer(f,700)*10**5,2) for f in fglist]
print(tlist)
print()

