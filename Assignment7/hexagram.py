def hex_dec(hex):
    #TODO: Implement this function
    hexCode = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,'A': 10, 'B': 11, 'C':12, 'D':13, 'E':14, 'F':15}
    sum = 0
    length = len(hex)
    for i in range(len(hex)):
        sum += 16**(len(hex)-(i+1))* hexCode[hex[i]]
    return sum

if __name__=="__main__":
    hex = str(input("Hex: "))
    print(hex_dec(hex))