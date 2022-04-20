# CBSE Probability Grade 9
# Example 7

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
Given the percentage of marks obtained by a student in monthly unit tests, find the probability that the student gets more than 70% marks in a unit test.
"""

import numpy as np
import pandas as pd

def main():
    df = pd.read_excel(r'../tables/table-1.xlsx')
    rows = np.array(df)
    all_outcomes = rows[0][1:]
    print(f'The theoretical probability is {theorProb(all_outcomes, 70)}')
    print(f'The empirical probability is {empProb(500, 70)}')

def theorProb(arr, cutoff):
    """ 
    Returns the theoretical probability that the student gets more than "cutoff" given the list of scores "arr"
    """
    desired_outcomes = [e for e in arr if e > cutoff]
    return len(desired_outcomes)/len(arr)

def empProb(trials, cutoff):
    """
    Returns the empirical probability that the student gets more than "cutoff" after "trials" number of random trials
    Note that this assumes that obtaining each percentage score is equally likely, which is very likely not the case
    """
    arr = np.random.randint(101, size=trials)
    desired_outcomes = [e for e in arr if e > cutoff]
    return len(desired_outcomes)/len(arr)

if __name__ == '__main__':
    main()
