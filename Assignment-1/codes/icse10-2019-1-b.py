# ICSE 2019 Grade 10
# Question 1(b)

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
A man invests Rs 4500 in shares of a company which is paying 7.5% dividend. If Rs 100 shares are available at a discount of 10%, find:
(i) the number of shares he purchases
(ii) his annual income
"""

def main():
    P = 4500    # Total investment made by the man
    F = 100     # Face value of a share
    d = 10      # Discount at which the shares are available
    D = 7.5     # Dividend

    # Output
    print(f"The man purchased {numberOfShares(P, F, d)} shares")
    print(f"The annual income of the man is Rs {format(annualIncome(P, D, d), '.2f')}")

def numberOfShares(investment, faceValue, discount) -> int:
    """ Returns the number of shares purchased """
    return int((100 * investment) // (faceValue * (100 - discount)))

def annualIncome(investment, dividend, discount) -> float:
    """ Returns the annual income earned """
    return (investment * dividend) / (100 - discount)

if __name__ == '__main__':
    main()