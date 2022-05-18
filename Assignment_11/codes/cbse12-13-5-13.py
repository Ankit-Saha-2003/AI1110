# CBSE Probability Grade 12
# Exercise 13.5.13

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
It is known that 10% of certain articles manufactured are defective. 
What is the probability that in a random sample of 12 such articles, 9 are defective?
"""

import matplotlib.pyplot as plt
from scipy.stats import binom

n = 12
p = 0.1

# Answer
print(binom.pmf(9, n, p))

# Plot
X = list(range(n + 1))
Y = binom.pmf(X, n, p)
plt.stem(X, Y, linefmt='r-', markerfmt='ro', basefmt='k--')
plt.title('Probability Mass Function')
plt.xticks(X)
plt.xlabel('$Y$')
plt.ylabel('Probability')
plt.savefig('../figs/fig-1.png')
plt.show()