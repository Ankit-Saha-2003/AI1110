# Papoulis Exercise 9-21

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
Show that if X(t) is a stationary process with derivative X′(t), then for a given t the random variables X(t) and X′(t) are orthogonal and uncorrelated
"""

import math
import numpy as np
from scipy.stats import norm
import random

t = random.randint(1, 100)
x = np.linspace(-3, 3, 1000)
X = norm.pdf(x) * math.sin(t)
dX = norm.pdf(x) * math.cos(t)    # d(sin(t))/dt = cos(t)

print(f't = {t}')
print(f"E[X(t)] = {sum(X*x)}")
print(f"E[X'(t)] = {sum(dX*x)}")
print(f"R_xx'(t,t) = E[X(t)X'(t)] = {sum(X*dX*x)} => Orthogonal")
print(f"C_xx'(t,t) = R_xx'(t,t) - E[X(t)]E[X'(t)] = {sum(X*dX*x) - sum(X*x) * sum(dX*x)} => Uncorrelated" )
