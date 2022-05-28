# Papoulis Exercise 4-35

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
If k1 + k2 + k3 = n, p1 + p2 + p3 = 1, k1*p1 << 1, k2*p2 << 1 then show that as n tends to infinity
n!/(k1!*k2!*k3!) = n^(k1+k2)/(k1!*k2!) and p3^k3 = exp(-n(p1+p2))
"""

from math import exp

n = 1e6
k1 = 5
k2 = 10
k3 = n - k1 - k2

p1 = 1e-6
p2 = 2e-6
p3 = 1 - p1 - p2

def factorial(x):
    ans = 1
    for i in range(2, x + 1): ans *= i
    return ans

prod = n
for i in range(1, k1 + k2): prod *= n - i
lhs_1 = prod / (factorial(k1) * factorial(k2))
rhs_1 = (n**(k1 + k2)) / (factorial(k1) * factorial(k2))
print(f'{lhs_1} {rhs_1}')
print(abs(lhs_1 - rhs_1) / lhs_1)

print('')

lhs_2 = p3**k3
rhs_2 = exp(-1*n*(p1 + p2))
print(f'{lhs_2} {rhs_2}')
print(abs(lhs_2 - rhs_2) / lhs_2)