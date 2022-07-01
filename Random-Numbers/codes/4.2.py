# Loads the t.dat file and plots the empirical and theoretical CDF of the random variable T

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt

values = np.loadtxt('t.dat', dtype='double')
NUM = len(values)
X1 = np.linspace(-1, 3, 30)
X2 = np.linspace(-1, 3, 100)
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
    elif x <= 1:
        the_cdf.append(x**2/2.0)
    elif x < 2:
        the_cdf.append(2*x - x**2/2.0 - 1)
    else:
        the_cdf.append(1)

plt.plot(X2, the_cdf, label='Theoretical')
plt.plot(X1, emp_cdf, 'o', label='Empirical')
plt.grid()
plt.legend()
plt.savefig('../figs/4.2.png')
plt.show()
