import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

a = np.random.randint(9, size=(5,5))

sum = 0

for i in a:
    for j in i:
        sum += j
ave = sum/25

for i in range(0, a.shape[0]):
    for j in range(0, a.shape[1]):
        if a[i][j] >= ave:
            plt.plot(i,j,'bo')
        else:
            plt.plot(i,j,'rx')

plt.show()
