# Input Parameter: dollar amount x2
# Return Value: list of quarters, dimes, nickels, and pennies (in that←↩order)

# importing stuff
import math

# function
def dollars(x):
    # create array return
    total = x
    sum = [0.0,0.0,0.0,0.0]
    rates = [.25, .10, .05, .01]
    # find coin totals
    for i in range(len(sum)):
        sum[i] += total // rates[i]
        total -= sum[i] * rates[i]
        
    return sum

# Test Zone
print(dollars(2.24))
print(dollars(1.19))
print(dollars(4.19))

# Auto grader setup
if __name__ == 'main':
    pass