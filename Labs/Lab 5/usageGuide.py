import matplotlib.pyplot as plt
import numpy as np
import pandas

fig = plt.figure() # empty figure with no axes
fig.suptitle('No axes on this figure') # add a title so we know which it is

fig, ax_lst = plt.subplots(2,2) # figure w/ 2x2 grid of axes

a = pandas.DataFrame(np.random.rand(4,5), columns = list('abcde'))
a_asarray = a.values
print(a_asarray)

# convert to matric
b = np.matrix([[1,2],[3,4]])
b_asarray = np.array(b)
print(b_asarray)

# Matplotlib pyplot and pylab -> how are they related
x=np.linspace(0,2,100)

plt.plot(x,x, label='linear')
plt.plot(x,x**2, label='quadratic')
plt.plot(x,x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title('simple plot')

plt.legend()

plt.show()
# it is recommended to use pyplot to create non-interactive figures