# Plotting Y = AX + N

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt

Y = np.loadtxt('y.dat', dtype='double')
NUM = len(Y)
X = range(0, NUM)

plt.plot(X, Y, 'o')
plt.grid()
plt.savefig('../figs/5.3.png')
plt.show()
