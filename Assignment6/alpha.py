d = {}
#Marvelous code
with open('happy.txt', 'r') as happy:
    while 1:
        char = happy.read(1).lower()     # read by character
        if not char: 
            break
        if ord(char) > 60 and d.get(char, 0) < 1:
            d[char] = 1
        elif d.get(char, 0) >= 1:
            d[char] += 1
    for key,value in sorted(d.items()):
        print(key, ':', value)
    happy.close()

if __name__ == "__main__":
    pass