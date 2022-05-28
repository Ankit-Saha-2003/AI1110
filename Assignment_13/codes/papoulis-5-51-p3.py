# Papoulis Exercise 5-51

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
A box contains N identical items of which M < N are defective ones. 
A sample of size n is taken from the box without replacement, and let X represent the number of defective items in the sample.
Show that as N, M tend to infinity with M/N tending to p (0 < p < 1) the hypergeometric distribution tends to the binomial distribution provided n << N
"""

import matplotlib.pyplot as plt
from scipy.stats import hypergeom, binom

N = 1e6
M = 0.25e6
n = 10
p = M/N

X = list(range(n+1))
rv = hypergeom(N, n, M)
hyp = rv.pmf(X)
bnm = binom.pmf(X, n, p)

# Plotting the PMF
plt.stem(X, hyp, linefmt='k--', markerfmt='ro', basefmt='k--', label='Hypergeometric')
plt.stem(X, bnm, linefmt='k--', markerfmt='bo', basefmt='k--', label='Binomial')
plt.title('Hypergeometric vs Binomial Distribution')
plt.xticks(X)
plt.xlabel('$X$')
plt.ylabel('Probability')
plt.legend()
plt.show()

