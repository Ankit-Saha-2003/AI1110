# Loads the uni.dat file and plots the empirical CDF of the uniform random variable in [0,1]

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt

values = np.loadtxt('uni.dat', dtype='double')
NUM = len(values)
X1 = np.linspace(-1, 2, 30)
X2 = np.linspace(-1, 2, 100)
emp_cdf = []
the_cdf = []

for x in X1:
    count = 0
    for value in values:
        if value <= x:
            count += 1
    emp_cdf.append(count/NUM)

for x in X2:
    if x < 0:
        the_cdf.append(0)
    elif x > 1:
        the_cdf.append(1)
    else:
        the_cdf.append(x)

plt.plot(X2, the_cdf, label='Theoretical')
plt.plot(X1, emp_cdf, 'o', label='Empirical')
plt.grid()
plt.legend()
plt.savefig('../figs/1.2.png')
plt.show()
