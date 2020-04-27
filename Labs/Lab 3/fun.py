### You will complete the following 5 functions (in fun.py): 
### 1. Implement factorial using for-loop. (If they are unsure, they can ask for help.)
### 2. Implement a function that checks the number of letter "a" in a string. 
### 3. Implement multiplication as a function, using for-loop. Test mul(4,5) = 20
### 4. Implement division as a function, using for-loop. test div(7,3) = 2
### 5. Implement "modulo" as a function, using for-loop, minus-, and less than<.  test mod(20,6) = 2

# for loop structure
# Examples of containers: Lists
# container = ['This', 'is', 'a', 'container']
# for item in container:
#     print(item)

def factorial(n):
    # go up by 1 every loop
    total = 1
    # range(start,end,step)
    for x in range(1, n + 1):
        total *= x
    return total

def aNum(string):
    count = 0
    for a in range(len(string)):
        if(string[a] == 'a'):
            count += 1
    return count

def mul(x, y):
    # x is number 
    # y is how many
    sum = 0
    for l in range(y):
        sum += x
    return sum

def divide(x, y):
    count = 0
    result = x
    for l in range(y):
        count += 1
        result -= y
        if((result - y) < 0):
            break
    return count
    
def modulo(x, y):
    count = 0
    result = x
    for l in range(y):
        count += 1
        result -= y
        if((result - y) < 0):
            break
    return result
