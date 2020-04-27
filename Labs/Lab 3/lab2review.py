# Better ways to solve problems from last lab

#Create helper function for maxThree function
def maxTwo(x, y):
    if x > y:
        return x
    else: 
        return y

def maxThree(x, y, z):
    return maxTwo(maxTwo(x, y), z)

def maxTwoSum(x, y, z):
    # Find max of the 3 sums
    sum1 = x + y
    sum2 = x + z
    sum3 = y + z
    # reuse the function already built above!
    return maxThree(sum1, sum2, sum3)

# Min would be a similar approach, but of course finding the minimum

def minTwoSum(x, y, z):
    sum = x + y + z
    return sum - maxThree(x, y, z)

print([1] + [2])