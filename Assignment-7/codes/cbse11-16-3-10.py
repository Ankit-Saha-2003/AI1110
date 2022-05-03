# CBSE Probability Grade 11
# Exercise 16.3.10

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
A letter is chosen at random from the word 'ASSASSINATION'. Find the probability that the letter is:
(i) a vowel
(ii) a consonant
"""

import matplotlib.pyplot as plt
import requests
import random

WORDS = requests.get('https://www.mit.edu/~ecprice/wordlist.10000').content.splitlines()

def main():
    word = 'ASSASSINATION'
    print(f'The probability that a randomly chosen letter from {word} is a vowel is {probVowel(word)}')
    print(f'The probability that a randomly chosen letter from {word} is a consonant is {1 - probVowel(word)}\n')
    plotPMF(word)

    # Computing probabilities for a random word
    rand_word = str(random.choice(WORDS))
    word = rand_word[2:-1]
    print(f'The probability that a randomly chosen letter from {word.upper()} is a vowel is {probVowel(word.upper())}')
    print(f'The probability that a randomly chosen letter from {word.upper()} is a consonant is {1 - probVowel(word.upper())}')

def probVowel(word):
    """
    Returns the probability that a randomly chosen letter from 'word' is a vowel
    """
    vowels = 0
    vowels += word.count('A')
    vowels += word.count('E')
    vowels += word.count('I')
    vowels += word.count('O')
    vowels += word.count('U')
    return float(format(vowels/len(word), '.3f'))

def plotPMF(word):
    """
    Plots the probability mass function for the probability distribution of vowels and consonants in 'word'
    """
    X = list(range(2))
    Y = [probVowel(word), 1 - probVowel(word)]
    plt.stem(X, Y, linefmt='r-', markerfmt='ro', basefmt='k--')
    plt.title('Probability Mass Function')
    plt.xticks(X)
    plt.xlabel('$X$')
    plt.ylabel('Probability')
    plt.show()

if __name__ == '__main__':
    main()