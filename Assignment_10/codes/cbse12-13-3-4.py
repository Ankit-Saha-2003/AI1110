# CBSE Probability Grade 12
# Exercise 13.3.4

# Name: Ankit Saha
# Roll number: AI21BTECH11004

"""
Problem Statement
In answering a question on a multiple choice test, a student either knows the answer or guesses. 
Let 3/4 be the probability that he knows the answer and 1/4 be the probability that he guesses. 
Assuming that a student who guesses at the answer will be correct with a probability 1/4. 
What is the probability that the student knows the answer given that he answered it correctly?
"""

import numpy as np
import pandas as pd

# Preparing the data
df = pd.read_excel(r'../tables/table-2.xlsx')
data = np.array(df)
probs = dict(zip(data[:,0], data[:,1]))

# Computing the probability
pr = (probs['Pr(X = 1|Y = 0)'] * probs['Pr(Y = 0)']) / (probs['Pr(X = 1|Y = 0)'] * probs['Pr(Y = 0)'] + probs['Pr(X = 1|Y = 1)'] * probs['Pr(Y = 1)'])
print(format(pr, '.3f'))