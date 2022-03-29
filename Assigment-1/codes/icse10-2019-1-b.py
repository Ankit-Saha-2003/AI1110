# ICSE 2019 Grade 10
# Question 1(b)

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
A man invests Rs 4500 in shares of a company which is paying 7.5% dividend. If Rs 100 shares are available at a discount of 10%, find:
(i) the number of shares he purchases
(ii) his annual income
"""

P = 4500    # Total investment made by the man
F = 100     # Face value of a share
d = 10      # Discount at which the shares are available
D = 7.5     # Dividend

# Market value of a share
M = F * (1 - d * 0.01)

# The number of shares purchased
N = int(P // M)

# His annual income
A = F * N * D * 0.01

# Output
print(f"The man purchased {N} shares")
print(f"The annual income of the man is Rs {A}")