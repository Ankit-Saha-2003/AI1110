# Plots theoretical and empirical P_e with respect to gamma from 0 to 10 dB

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import scipy

p_e = np.loadtxt('7.1.dat', dtype='double')
NUM = len(p_e)
gamma = np.linspace(0, 10, 41)

def P_e_Rayleigh(gamma):
    tmp = gamma/(gamma + 2)
    return 0.5 * (1 - tmp**0.5)

vec_p_e = scipy.vectorize(P_e_Rayleigh, otypes=[float])

plt.plot(gamma, vec_p_e(gamma), label='Theoretical')
plt.plot(gamma, p_e, 'o', label='Empirical')
plt.grid()
plt.legend()
plt.xlabel('$\gamma$')
plt.ylabel('$P_e$')
plt.savefig('../figs/7.1.png')
plt.show()
