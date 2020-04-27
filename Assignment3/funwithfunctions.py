import math

#1 
def y(d,r,t):
    #TO DO: IMPLEMENT FUNCTION
    return d * math.exp(r*t)
#2
def N(n_0, m, t):
    #TO DO: IMPLEMENT FUNCTION
    return n_0 * math.exp(m * t)
#3
def N_t(t):
    #TO DO: IMPLEMENT FUNCTION
    const = 71.8
    const_2 = -8.96
    const_3 = -.0685
    return const * math.exp(const_2 * math.exp(const_3*t))
#4
def K(t):
    #TO DO: IMPLEMENT FUNCTION
    numerator = ((9 / 2.6) * t )
    denominator = 2 * t**2 + 3
    return numerator / denominator
#5
def r(t):
    #TO DO: IMPLEMENT FUNCTION
    x4 = 1.5207
    x3 = 19.166
    x2 = 62.91
    x1 = 6.0726
    x0 = 1026
    return x4 * t**4 - x3*t**3 + x2 * t**2 + x1 * t**1 + x0
#6
def p(x):
    #TO DO: IMPLEMENT FUNCTION
    return 4* x**2 - 100 * x - 1000
#7
def W(P_i,P_f):
    #TO DO: IMPLEMENT FUNCTION
    return 8.314 * 300 * math.log(P_i / P_f)
#8
def depreciate(c,s,life):
    #TO DO: IMPLEMENT FUNCTION
    return (c - s) / life
#9
def L(k,V,A,C):
    #TO DO: IMPLEMENT FUNCTION
    return k * V**2 * A * C

print(y(1000,.02,10))
print(N(500,100,4))
print(math.floor(N_t(1000)))
print(K(1))
print(r(4))
print(p(10))
print(W(10,1))
print(depreciate(20000,1000,5))
print(L(0.0033,33.8,512,0.515))
if __name__=="__main__":
    print('hello world')