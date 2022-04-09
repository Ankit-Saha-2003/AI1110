# ICSE 2019 Grade 12
# Question 1(ii)

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
Solve: sin(2arctan(x)) = 1
"""

import numpy as np
import matplotlib.pyplot as plt

# Preparing to plot y = sin(2arctan(x))
coords = np.loadtxt('points.dat', dtype='float')
X = []
Y = []
for coord in coords:
    X.append(coord[0])
    Y.append(coord[1])

# Preparing to plot y = 1
X2 = np.linspace(-6, 6, 1200)
Y2 = np.linspace(1, 1, 1200)

# Plotting
plt.plot(X, Y, label='$y = \sin(2\\tan^{-1}x)$')
plt.plot(X2, Y2, label='$y = 1$')

# Displaying the solution
sol = np.zeros((2,1))
sol[0][0] = 1
sol[1][0] = 1
A = sol[0]
B = sol[1]
plt.plot(A, B, 'o')
for xy in zip(A, B):
    plt.annotate('(%s, %s)' %xy, xy=xy, xytext=(30, 0), textcoords='offset points')

plt.grid()
plt.legend(loc='best', prop={'size':11})
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()