import math

# INPUT function fn, start is a, end is b,
# n is an even number of intervals

# RETURN approximate area under the curve
def simpson(fn,a,b,n):
    delta_x = (b - a)/n
    interval = lambda i: a + i*delta_x                  # put this in the function argument
    approximation = 0
    # Assign approximation
    for i in range(0, n+1):
        if(i == 0):                 # zero
            approximation += fn(a)
        elif(i % 2 == 0 and i != n):           # even
            approximation += (2 * fn(interval(i)))
        elif(i % 2 == 1 and i != n):            # odd
            approximation += (4 * fn(interval(i)))
        else:                                   # i == n
            approximation += fn(b)
    return approximation * ((b - a) / (3 * n))
    

# convert string to either number or expression
def convert(x):
    if x.isnumeric():
        return float(x)
    else:
        return eval(x)
        
with open("Assignment8/integralfile.txt", "r") as xfile:
    xlines = [d.split(",") for d in xfile.read().split("\n")]
    

for i in xlines:
    body = i[0]
    fn = eval("lambda x : " + body)         # valid function can be called
    a = convert(i[1])
    b = convert(i[2])
    n = convert(i[3])
    answer = convert(i[4])
    integration = simpson(fn,a,b,n)
    error = abs((answer - integration)/answer)
    print("f(x) = {0} over [{1},{2}] is {3:.3f}".format(body,a,b,integration))
    print("Actual answer is {0:.3f}".format(answer))
    print("Error is {0:.3f}".format(error))