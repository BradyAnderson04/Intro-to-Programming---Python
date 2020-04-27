# Input value: some number
# Output value: the result of the magical encantation

def magic(x):
    return (((((x+15) * 3) - 9) / 3) - 12)
    

if __name__=="__main__":
    #get input
    x = input("Pick any positive whole number: ")
    
    #change from string to integer
    x = int(x)

    print("Your number was", magic(x))

# ex: 2
'''
2 + 15 = 17
17 * 3 = 51
51 - 9 = 42
42 / 3 = 14
14 - 12 = 2


mess w/ ratio 

So while subract more than you add, you added a larger ratio of the number
Effectively you are subtracting the same ratio

'''