# CBSE Probability Grade 10
# Exercise 15.1.10

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
A piggy bank contains hundred 50 p coins, fifty Rs 1 coins, twenty Rs 2 coins and ten Rs 5 coins. 
If it is equally likely that one of the coins will fall out when the bank is turned upside down, what is the probability that the coin:
(i) will be a 50 p coin
(ii) will not be a Rs 5 coin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Reading data
df = pd.read_excel(r'data.xlsx')
data = np.array(df)

# Computing the probabilities
total = sum(data[1])
probs = [n/total for n in data[1]]
print(f"The probability that the coin will be a 50 p coin is {format(probs[0], '.3f')}")
print(f"The probability that the coin will not be a Rs 5 coin is {format(probs[0] + probs[1] + probs[2], '.3f')}")

# Plotting the PMF
plt.stem(data[0], probs, linefmt='r-', markerfmt='ro', basefmt='k--')
plt.title('Probability Mass Function')
plt.xlabel('$X$')
plt.ylabel('Probability')
plt.show()