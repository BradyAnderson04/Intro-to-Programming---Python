'''
Overview:
I am trying to explore the mathmatical theorems explored in book How to Prove it

Goals:
1.See how these behave in a reasonable computational sense
2.Define the reasons why this happens
3.Apply princples learned in other aspects of exploration and discuss w/ Proffesors

Overall Importance:
I am Brady Anderson and I am greatly interested in the nature of conciousness. This specifically deals with how we process reality going into how we explore and comprehend new ideas


'''

# Exercise 1

value = (2 **15) - 1
print(value)

values = [2, 3, 4, 5, 6, 7, 8, 9, 10]
def factor(num):
    for i in range(2, num + 1):
        if(num % i == 0):
            return 'Not Prime' 
    return 'Prime'
print(factor(value))
# find values that prove the value is not prime

# conjecture time
for i in range(20):
    a = 3**i - 1
    b = 3**i - 2**i
    print('{0} {1} {2}'.format(a, b, factor(a) and factor(b))) 

'''
A number is not prime is a number is greater than 2 and even
A number is prime when 1 times the number is equal to the number
A number is prime when the number divided by an integet != an integer
'''