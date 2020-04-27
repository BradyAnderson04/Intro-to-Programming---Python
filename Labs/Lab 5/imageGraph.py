import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('dog.png')
print(img)
imgplot = plt.imshow(img)
plt.show()