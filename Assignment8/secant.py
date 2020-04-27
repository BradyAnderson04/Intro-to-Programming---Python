# function
f = lambda x: x**6 - x - 1
# method
# method = eval(input('Pick 0, 1, or 2: '))

d = {}
def secant(f,x0,x1,tau):
    # TO DO: Implement function
    # Use the following print statement to display the data nicely

    # caclulate current guess, then calculate next value
    d[0] = x0
    d[1] = x1
    # if(method == 0):
        # for loop
    for i in range(2, 8):
        d[i] = d[i-1] - (f(d[i-1]) * ( (d[i-1] - d[i-2]) / (f(d[i-1]) - f(d[i-2]))) )
        print("{0:.5f} {1:.5f} {2:.5f} {3:.5f}".format(d[i-2],f(d[i-2]),f(d[i-1]),d[i-2]-d[i-1]))
    # else:
    #     # recursion
    #     i = 0
    #     if(i < 2):
    #         i += 1
    #         return d[i]
    #     else:
    #         d[i] = d[i-1] - (f(d[i-1]) * ( (d[i-1] - d[i-2]) / (f(d[i-1]) - f(d[i-2]))) )
    #         print("{0:.5f} {1:.5f} {2:.5f} {3:.5f}".format(d[i-2],f(d[i-2]),f(d[i-1]),d[i-2]-d[i-1]))
    #         return secant(d[i-2],f(d[i-2]),f(d[i-1]),d[i-2]-d[i-1])

         
    


secant(f,2.0,1.0,.0001)