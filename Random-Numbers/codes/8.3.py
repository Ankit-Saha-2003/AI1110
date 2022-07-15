# Plots theoretical and empirical P_e with respect to SNR from 0 to 10 dB

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import scipy

p_e = np.loadtxt('8.3.dat', dtype='double')
snr = np.linspace(0, 10, 41)

def Q_function(x):
    return 0.5 * mp.erfc(x/(2**0.5))

def P_e_2D(snr):
    return Q_function(np.sqrt(snr/2))

vec_p_e = scipy.vectorize(P_e_2D, otypes=[float])

plt.plot(snr, vec_p_e(snr), label='Theoretical')
plt.plot(snr, p_e, 'o', label='Empirical')
plt.grid()
plt.legend()
plt.xlabel('SNR')
plt.ylabel('$P_e$')
plt.savefig('../figs/8.3.png')
plt.show()
