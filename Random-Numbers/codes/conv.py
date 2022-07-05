# Testing if the convolution gives a triangular distribution or not

import numpy as np
import matplotlib.pyplot as plt

A = [1.0/6] * 6
Y = np.convolve(A, A)
X = np.linspace(2, 12, 11)
plt.plot(X, Y)
plt.grid()
plt.xticks(range(2, 13))
plt.show()
