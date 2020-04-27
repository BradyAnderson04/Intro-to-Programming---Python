# Importing your own files
from lab2 import add
# Importing 3rd party libraries
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as mplp
'''
Import basically puts the top of the code at the top of the file
This will run any code from that file and compile with the file
We do this to have more organized structure of code
-> very useful tip!
'''

# Matplotlab testing out -> need to do import matplotlib.pyplot
# mpl.plot([1,3,4,10,14], [3, 1, 20, 3, 2], 'red')
# mpl.show()

if __name__ == '__main__':
    print(add(4,10))
    print(add(2, 1))

print('Lab1 name: ' + __name__)
