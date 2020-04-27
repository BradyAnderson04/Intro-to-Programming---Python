# use only for loops and print statements

# Triangle one
def triangleOne():
    for i in range(10):
        print('*' * i)
    for i in range(8, 0, -1):
        print('*' * i)
    return ''

# Triangle Two -> drawback if you don't know all the values you want to include...I couldn't figure out the pattern
length = {0:1, 1:3, 2:6, 3:10, 4:15, 5:21, 6:28, 7:36, 8:45}
def triangleTwo():
    for i in length:
        print(length[i] * '*')
    for j in range((len(length) - 1), 0, -1):
        print(length[j - 1 ] * '*')
    return ''



# Triangle Three
def triangleThree():
    count = 0
    for i in range(10, -1, -1):
        print(' ' * count +((i * 2 + 1) * '*'))
        count += 1
    return ''

#tests
print(triangleOne())
print(triangleTwo())
print(triangleThree())

# checking things here
# print(len('*********************************************'))
# print(len('************************************'))
# print(len('****************************'))
# print(len('*********************'))
# print(len('***************'))
# print(len('**********'))
# print(len('******'))
# print(len('***'))
# print(len('*********************'))
# print(len('*******************'))
# print(len('*****************'))

# Auto Grader
if __name__ == 'main':
    pass