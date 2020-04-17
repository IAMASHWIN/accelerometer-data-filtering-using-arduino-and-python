import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
z = pd.read_csv('data.csv')
k = list(z['0'])
N = 11


def fmag(y, hdn):
    yp = []
    for i in range(len(y)):
        temp = 0
        for j in range(len(hdn)):
            if (i-j >= 0):
                temp += hdn[j]*y[i-j]
        yp.append(temp)
    return yp


hdn = []
for i in range(-5, 6):
    a, b = quad(lambda w: np.cos(w*i) + 1j*np.sin(w*i), -np.pi, np.pi)
    hdn.append(a/6.28)
plt.subplot(811)
plt.plot(k)
plt.subplot(812)
plt.plot(fmag(k, hdn))
hdn1 = []
for i in range(-5, 6):
    a, b = quad(lambda w: np.cos(w*i) + 1j*np.sin(w*i), -3*np.pi/4, 3*np.pi/4)
    hdn1.append(a/6.28)
plt.subplot(813)
plt.plot(fmag(k, hdn1))
hdn2 = []
for i in range(-5, 6):
    a, b = quad(lambda w: np.cos(w*i) + 1j*np.sin(w*i), -np.pi/2, np.pi/2)
    hdn2.append(a/6.28)
plt.subplot(814)
plt.plot(fmag(k, hdn2))
hdn3 = []
for i in range(-5, 6):
    a, b = quad(lambda w: np.cos(w*i) + 1j*np.sin(w*i), -1*np.pi/4, 1*np.pi/4)
    hdn3.append(a/6.28)
plt.subplot(815)
plt.plot(fmag(k, hdn3))
plt.subplot(816)
plt.plot(np.abs(k))
plt.subplot(817)
plt.plot(np.abs(fmag(k, hdn3)))
plt.show()
