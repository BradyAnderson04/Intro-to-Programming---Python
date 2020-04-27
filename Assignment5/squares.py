'''
 
want to make a square that is as many lines as is wide
only first and last have star


'''

def sq(n):
    for i in range(n):
        if(i == 0 or i == (n-1)):
            print('*'*n)
        else:
            print('*', ' '*(n-4), '*')
            
sq(1)
print()
sq(2)
print()
sq(5)
print()
sq(6)