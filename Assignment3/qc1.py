#imports needed
import numpy as np
import math
import numpy as np
import matplotlib.pyplot as plt
#INPUT ax**2 + bx + c = 0 coefficients to quadratic
#RETURN tuple (x,y) that are solutions
def quadraticP(a, b, c):
    return (-b + math.sqrt(b**2 - 4 * a  * c)) / 2*a
    
def quadraticN(a, b, c):
    return (-b - math.sqrt(b**2 - 4 * a  * c)) / 2*a

def complexRoot(a, b, c):
    i = b**2 - 4 * a * c
    reg 

def q(a,b,c):
    #TO DO: IMPLEMENT FUNCTION

    if (b**2 - 4 * a * c) >= 0: # is positive
        pos = quadraticP(a, b, c)
        neg = quadraticN(a, b, c)
        print('Not complex')
        print(pos, neg)
    if(b**2 -4 * a * c) < 0: # is negative
        iCo = math.sqrt(abs((b**2 - 4 * a * c))) / (2 * a)
        num = -b / (2 * a)
        print('Complex')
        print (complex(num, iCo), complex(num, -iCo))
    return ""

# Tests
print(q(1,3,-4))
print(q(2,-4,-3))
print(q(9,12,4))
print(q(3,4,2))



# # Test & fun stuff!
# #assigns the two values into x and y
# #because this returns a tuple (firstvalue, secondvalue)
# x1,y1 = q(1,-2,-4) # x**2 - 2*x - 4 = 0
# print(x1,y1)
# #creates an anonymous function
# #this is the function described above
# #You should be intrigued by this assignment
# #What is it doing?
# f = lambda x:x**2 - 2*x - 4
# #the output should be zero
# print(f(x1),f(y1))

# # Plotting Porition
# # evenly sampled time at 200ms intervals
# x = np.arange(-4.0, 5.0, 0.2)
# # Green dashes for line
# plt.plot(x, x**2 - 2*x - 4,’g--’)
# # Blue dashes for line
# plt.plot(x,3*x**2 + 4*x + 2,’b--’)
# # Draw horizontal line
# plt.plot([-4,4],[0,0], color=’k’, linestyle=’-’, linewidth=2)
# # Plot red dots as solution
# plt.plot([x1,y1],[0,0],’ro’)
 if __name__=="__main__":
     plt.show()