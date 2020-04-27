def vol(x,y,z):
    return x*y*z == 147840

# Calc heat loss
def f(x,y,z):
    return 11*x*y + 14*y*z + 15*x*z

# create var to store optimal value -> really big for arbitrary purposes
minLoss = 100000000000  
#some arbitrary starting point
a,b,c = 2,2,36960 

# Create loop to go through every value specifies
for i in range(0, 101):
    for j in range(0, 101):
        for k in range(0, 101):
            if(f(i, j, k) < minLoss and vol(i,j,k)):
                a,b,c = i,j,k
                minLoss = f(i,j,k)
                
    
#TO DO: LOOPS SEARCHING THROUGH POSSIBLE VALUES

print("H W L Value")
print(a,b,c,f(a,b,c))

if __name__ == "main":
    pass


# heat loss equation for a building -> regardless of shape
# 11xy+ 14yz+ 15xz