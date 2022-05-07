import numpy as np

X = list(range(1,7))

nE = 0
nE += X.count(3)
nE += X.count(6)

nF = 0
nF += X.count(2)
nF += X.count(4)
nF += X.count(6)

nEF = 0
nEF += X.count(6)

pE = nE/len(X)
pF = nF/len(X)
pEF = nEF/len(X)

err = 1e-4 # To account for floating point error

if (abs(pEF - pE*pF) < err): print('E and F are independent')
else: print('E and F are dependent')

# Random experiment
trials = 600
X = np.random.randint(1, 7, size=trials)

nE = 0
nE += np.count_nonzero(X == 3)
nE += np.count_nonzero(X == 6)

nF = 0
nF += np.count_nonzero(X == 2)
nF += np.count_nonzero(X == 4)
nF += np.count_nonzero(X == 6)

nEF = 0
nEF += np.count_nonzero(X == 6)

pE = nE/len(X)
pF = nF/len(X)
pEF = nEF/len(X)

print(pEF)
print(pE*pF)
print(abs(pEF - pE*pF))