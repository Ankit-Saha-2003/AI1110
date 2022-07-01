# Loads the gau.dat file and plots the empirical and theoretical CDF of the Gaussian random variable in [-6,6]

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

values = np.loadtxt('gau.dat', dtype='double')
NUM = len(values)
X1 = np.linspace(-7, 7, 30)
X2 = np.linspace(-7, 7, 100)
emp_cdf = []
the_cdf = []

for x in X1:
    count = 0
    for value in values:
        if value <= x:
            count += 1
    emp_cdf.append(count/NUM)

def Q_function(x):
    return 0.5 * mp.erfc(x/(2**0.5))

for x in X2:
    the_cdf.append(1 - Q_function(x))

plt.plot(X2, the_cdf, label='Theoretical')
plt.plot(X1, emp_cdf, 'o', label='Empirical')
plt.grid()
plt.legend()
plt.savefig('../figs/2.2.png')
plt.show()
