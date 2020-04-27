method = eval(input('Enter 0, 1, or 2: '))
f = lambda x: x**6 - x - 1

def sign(x):
    # TO DO: Implement this function
    if(x > 0):
        return 1
    else:
        return -1



def bisect(f,a,b,tau):
    # TO DO: Implement this function
    # Use the following print statement to display the data nicely
    # the c variable is from the algorithmic specification of the←↩bisection method seen above
    '''
    calculate C
    check condition
    change C based off values

    '''
    c = (a + b)/2
    if(method == 0):
        # while method
        while(b - c <= tau):
            if(sign(f(b)) * sign(f(c)) <= 0):
                a = c
            else:
                b = c
        return c
    elif(method == 1):
        # for loop time
        for i in range(20):
            if(b - c <= tau):
                return c
            else:
                if(sign(f(b)) * sign(f(c)) <= 0):
                    a = c
                else:
                    b = c
                return c
    else:
        # recursion baby!
        if(b - c <= tau):
            return c
        else:
            if(sign(f(b)) * sign(f(c)) <= 0):
                a = c
            else:
                b = c
            return bisect(f,a, b, tau)
            
    print("{0:.5f} {1:.5f} {2:.5f} {3:.5f} {4:.5f}".format(a,b,c,b-c,f(c)))
    
    
print(bisect(f,1.0,2.0,.001))