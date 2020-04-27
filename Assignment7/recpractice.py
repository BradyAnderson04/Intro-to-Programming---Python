from datetime import datetime

def s(n):
    #TODO: Implement function
    if(n == 0):
        return 0
    else:
        return s(n-1) + n
    
def s1(n):
    #TODO: Implement function
    return (n * (n-1))/ n
    
def p(n):
    #TODO: Implement function
    if(n == 0):
        return 10000
    else:
        return p(n-1) + p(n-1) * .02 
    
def p1(n):
    #TODO: Implement function
    return (1.02)**n * 10000
    
def b(n):
    #TODO: Implement function
    if(n == 1):
        return 2
    elif(n == 2):
        return 3
    else:
        return b(n-1) + b(n-2)
    
def c(n):
    #TODO: Implement function
    if(n == 1):
        return 9
    else:
        return 9* c(n-1) + 10**(n-1) - c(n-1)
    
def d(n):
    #TODO: Implement function
    if(n == 0):
        return 1
    else:
        return 3 * d(n-1) + 1
    
def d1(n):
    #TODO: Implement function
    return (3**(n+1) - 1) / 2
    
def c18(n,k):
    #TODO:Implement function - never seen notation ask Dr. D about that...
    if(n==k):
        return 1
    elif n == 0:
        return 1
    elif k > n:
        return 0
    else:
        return c18(n-1, k) + c18(n-1,k-1)

def B(n):
    #TODO:Implement function
    if(n == 0):
        return 1
    else:
        sum = 0
        for i in range(0,n):
            sum += c18(n+1, i) * B(i)
        return sum / (n+1) * (-1)
    
if __name__=="__main__":
    #TODO: Show the first ten values of each using one for loop inside←↩this if statement.
    for i in range(1,11):
        print(s(i))
        print(s1(i))
        print(p(i))
        print(p1(i))
        print(b(i))          
        print(c(i))
        print(d(i))
        print(d1(i))
        print(B(i))
        print('-'*8)
    pass
    # dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)	
    # print(p(30))
    # dt_string1 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string1)	
 



'''
1.It takes 5 minutes 22 seconds to calculate p(30) -> calculated w/ datetime
2.Kinda looks like the fibonachi sequence
'''