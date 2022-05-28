# Papoulis Exercise 5-51

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
A box contains N identical items of which M < N are defective ones. 
A sample of size n is taken from the box without replacement, and let X represent the number of defective items in the sample.
Find the hypergeometric probability distribution of X
"""

import matplotlib.pyplot as plt
from scipy.stats import hypergeom
import random

N = 100
M = 25
n = 10

# Theoretical distribution
rv = hypergeom(N, n, M)
X = list(range(n+1))
probs = rv.pmf(X)

# Simulation (empirical distribution)
items = [1] * M + [0] * (N-M) # 1 denotes defective and 0 denotes non-defective
random.shuffle(items)
counts = [0] * (n+1)
trials = 1000
for _ in range(trials):
    chosen_sample = random.sample(items, n) # Sampling without replacement
    counts[chosen_sample.count(1)] += 1/trials

# Plotting the PMF
plt.stem(X, probs, linefmt='k--', markerfmt='ro', basefmt='k--', label='Theoretical')
plt.stem(X, counts, linefmt='k--', markerfmt='bo', basefmt='k--', label='Empirical')
plt.title('Hypergeometric Distribution')
plt.xticks(X)
plt.xlabel('$X$')
plt.ylabel('Probability')
plt.legend()
plt.show()

