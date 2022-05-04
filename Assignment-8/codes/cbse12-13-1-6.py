# CBSE Probability Grade 12
# Exercise 13.1.6

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
A coin is tossed three times. Determine Pr(E|F) for the following three cases:
(i) E: head on third toss, F: heads on first two tosses
(ii) E: at least two heads, F: at most two heads
(iii) E: at most two tails, F: at least one tail
"""

import matplotlib.pyplot as plt
from scipy.stats import binom

n = 3
p = 0.5

# Computing the probabilities
print(f'(i) {p}')
print(f"(ii) {format(binom.pmf(2,n,p)/(binom.pmf(0,n,p) + binom.pmf(1,n,p) + binom.pmf(2,n,p)), '.3f')}")
print(f"(iii) {format((binom.pmf(1,n,p) + binom.pmf(2,n,p))/(binom.pmf(0,n,p) + binom.pmf(1,n,p) + binom.pmf(2,n,p)), '.3f')}")

# Plotting the probability mass function
X = list(range(n + 1))
Y = [binom.pmf(0,n,p), binom.pmf(1,n,p), binom.pmf(2,n,p), binom.pmf(3,n,p)]
plt.stem(X, Y, linefmt='r-', markerfmt='ro', basefmt='k--')
plt.title('Probability Mass Function')
plt.xticks(X)
plt.xlabel('$Y$')
plt.ylabel('Probability')
plt.show()
