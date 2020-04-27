x = True
y = False
z = 12
a = 10
b = not (x or not (x or y)) and True

##########1###########
if b:
    print("Happy")
elif not b and x:
    print("Valentines")
if not b and not x and not y:
    print("day!")

##########2###########
if (z > a) or (2*a > z):
    print("C200")
if (z < a) or (2*a < z):
    print("is bliss")

##########3###########
if  (x and y):
    print(a)

##########4###########
if (2 > z) or x:
    print("1")
if 2 == 1:
    print("2")
if y and not x:
    print("3")
if  y and x:
    print("4")

##########5###########
def f(x):
    if x == 4:
        return 100
    elif x ==3:
        return 10
    elif x == 2:
        return 1000
    else:
        return 100000

print(f(4))
print(f(3))
print(f(2))
print(f(1))
if __name__=="__main__":
    print('')