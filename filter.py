import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
z = pd.read_csv('data.csv')
k = list(z['0'])
N = 11
hdn = []
for i in range(-10, 11):
    a, b = quad(lambda w: np.cos(w*i) + 1j*np.sin(w*i), -1*np.pi/4, 1*np.pi/4)
    hdn.append(a/6.28)


def fmag(y):
    yp = []
    for i in range(len(y)):
        temp = 0
        for j in range(len(hdn)):
            if (i-j >= 0):
                temp += hdn[j]*y[i-j]
        yp.append(temp)
    return yp


op = fmag(k)

# plt.subplot(211)
plt.grid(True)
# plt.plot(k)
# plt.subplot(212)
plt.plot(op, color='red')
plt.show()
