f = lambda x: x**6 - x - 1
fp = lambda x: 6*(x**5) - 1
tau = eval(input('Insert a thresh hold: '))
x0 = eval(input('Insert an initial estimate: '))
bound = eval(input('Insert max number of loops: '))

def fpa(f):
    h = .000001
    return lambda x: (f(x+h)-f(x-h))/(2*h)
    
def newton(f,fp,x,tau):
    def n(x,i):
        while f(x) > tau:
            print("{0} {1:.5f} {2:.5f}".format(i,x,f(x)))
            x = x - f(x)/fp(x)
            i += 1
            if i == bound:
                print('Not converging w/ Tau.')
                break
        return x
    n(x,0)
    
newton(f,fp,x0,tau)