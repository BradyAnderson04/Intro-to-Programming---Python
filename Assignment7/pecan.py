appr = 355/113
cnt = 0    
def mypi():
    #TO DO: IMPLEMENT YIELD
    result = 0
    while True:
        result += 4 * ((-1)**cnt * (1 / (1 + 2*cnt)))
        yield result

# pi1 = mypi()
# for i in range(3180):
#     x1 = next(pi1)
#     print(abs(abs((x1 - appr)/appr)))
#     cnt +=1


x1 = mypi()
z = next(x1)
while ((abs((z - appr)/appr)) > .0001):
    cnt += 1
    print(cnt)
    z = next(x1)
        
print(cnt, z)