# Loads the chi.dat file and plots the empirical and theoretical CDF and PDF of the chi-squared random variable with 2 degrees of freedom 

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import scipy

values = np.loadtxt('chi.dat', dtype='double')
NUM = len(values)
X1 = np.linspace(0, 10, 30)
X2 = np.linspace(0, 10, 100)
emp_cdf = []
emp_pdf = [0.5]

for x in X1:
    count = 0
    for value in values:
        if value <= x:
            count += 1
    emp_cdf.append(count/NUM)

def chiCDF(x):
    if x >= 0:
        return 1 - np.exp(-0.5*x)
    else:
        return 0

for i in range(len(X1)-1):
    emp_pdf.append((emp_cdf[i+1] - emp_cdf[i]) / (X1[i+1] - X1[i]))

def chiPDF(x):
    if x >= 0:
        return 0.5 * np.exp(-0.5*x)
    else:
        return 0

vec_chi_cdf = scipy.vectorize(chiCDF, otypes=[float])
vec_chi_pdf = scipy.vectorize(chiPDF, otypes=[float])

plt.plot(X2, vec_chi_cdf(X2), label='Theoretical')
plt.plot(X1, emp_cdf, 'o', label='Empirical')
plt.grid()
plt.legend()
plt.savefig('../figs/6.1.png')
plt.show()

plt.plot(X2, vec_chi_pdf(X2), label='Theoretical')
plt.plot(X1, emp_pdf, 'o', label='Empirical')
plt.grid()
plt.legend()
plt.savefig('../figs/6.2.png')
plt.show()
