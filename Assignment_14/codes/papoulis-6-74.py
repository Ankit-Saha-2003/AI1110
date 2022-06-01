# Papoulis Exercise 6-42

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
We have a pile of m coins.
The probability of heads of the i'th coin equals p_i.
We select at random one of the coins, we toss it n times and heads shows k times.
Find the probability that we selected the rth coin.
"""

from scipy.stats import binom

m = 5
p = [0.3, 0.5, 0.9, 0.1, 0.2]
n = 10
k = 7
r = 3

def prob(x):
    return binom.pmf(k, n, x)

prob_array = list(map(prob, p))
print(prob(p[r-1]) / sum(prob_array))
