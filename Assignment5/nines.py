def div_9(n):
    sum = 0
    total = 0
    for i in range(len(str(n))):
        sum += int(str(n)[i])
    for j in range(len(str(sum))):
        total += int(str(sum)[j])
    return total == 9 or sum == 0
x = [99,0,18273645,22]

for i in x:
    print(div_9(i))