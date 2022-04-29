# CBSE Probability Grade 11
# Example 9

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
Let a sample space be S = {w1, w2, w3, w4, w5, w6}. Which of the following assignments of probabilities to each outcome are valid?
"""

import numpy as np
import pandas as pd

def main():
    df = pd.read_excel(r'data.xlsx')
    data = np.array(df)
    print(*[isValid(d) for d in data], sep='\n')

def isValid(P):
    """
    Checks if an assignment of probability P is valid or not \n
    Returns 'Valid' if valid and 'Invalid' otherwise
    """
    e = 0.00001 # To account for floating-point error
    invals = [prob for prob in P if prob < 0 or prob > 1]
    if len(invals) > 0: return 'Invalid'
    elif sum(P) < 1 - e or sum(P) > 1 + e: return 'Invalid'
    else: return 'Valid'

if __name__ == '__main__':
    main()
