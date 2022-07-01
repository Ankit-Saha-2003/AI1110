# Loads the gau.dat file and plots the empirical and theoretical PDF of the Gaussian random variable in [-6,6]

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt
from scipy import special

values = np.loadtxt('gau.dat', dtype='double')
NUM = len(values)
X1 = np.linspace(-7, 7, 30)
X2 = np.linspace(-7, 7, 100)
emp_cdf = []

for x in X1:
    count = 0
    for value in values:
        if value <= x:
            count += 1
    emp_cdf.append(count/NUM)

emp_pdf = [0]
for i in range(29):
    emp_pdf.append((emp_cdf[i+1] - emp_cdf[i]) / (X1[i+1] - X1[i]))

the_pdf = []
for x in X2:
    the_pdf.append(np.exp(-0.5 * (x**2)) / np.sqrt(2 * np.pi))

plt.plot(X2, the_pdf, label='Theoretical')
plt.plot(X1, emp_pdf, 'o', label='Empirical')
plt.grid()
plt.legend()
plt.savefig('../figs/2.3.png')
plt.show()
