# Loads the ray.dat file and plots the empirical and theoretical CDF and PDF of the Rayleigh random variable

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import scipy

values = np.loadtxt('ray.dat', dtype='double')
NUM = len(values)
X1 = np.linspace(0, 10, 30)
X2 = np.linspace(0, 10, 100)
emp_cdf = []
emp_pdf = [0]

for x in X1:
    count = 0
    for value in values:
        if value <= x:
            count += 1
    emp_cdf.append(count/NUM)

def rayCDF(x):
    if x >= 0:
        return 1 - np.exp(-0.5*x*x)
    else:
        return 0

for i in range(len(X1)-1):
    emp_pdf.append((emp_cdf[i+1] - emp_cdf[i]) / (X1[i+1] - X1[i]))

def rayPDF(x):
    if x >= 0:
        return x * np.exp(-0.5*x*x)
    else:
        return 0

vec_ray_cdf = scipy.vectorize(rayCDF, otypes=[float])
vec_ray_pdf = scipy.vectorize(rayPDF, otypes=[float])

plt.plot(X2, vec_ray_cdf(X2), label='Theoretical')
plt.plot(X1, emp_cdf, 'o', label='Empirical')
plt.grid()
plt.legend()
plt.savefig('../figs/6.3.png')
plt.show()

plt.plot(X2, vec_ray_pdf(X2), label='Theoretical')
plt.plot(X1, emp_pdf, 'o', label='Empirical')
plt.grid()
plt.legend()
plt.savefig('../figs/6.4.png')
plt.show()
