import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
z = pd.read_csv('data.csv')
k = list(z['0'])
N = 11
hdn = []
for i in range(-5, 6):
    a, b = quad(lambda w: np.cos(w*i) + 1j*np.sin(w*i), -1*np.pi/4, 1*np.pi/4)
    hdn.append(a/6.28)
wn = []
for i in range(11):
    # wn.append(0.5-(0.5*np.cos((2*np.pi*i)/(N-1))))
    # wn.append(0.54-(0.46*np.cos((2*np.pi*i)/(N-1))))
    # wn.append(1)
    wn.append(0.42-(0.5*np.cos((2*np.pi*i)/(N-1))) +
              (0.08*np.cos((4*np.pi*i)/(N-1))))

hn = np.array(wn)*np.array(hdn)


def fmag(y):
    yp = []
    for i in range(len(y)):
        temp = 0
        for j in range(len(hn)):
            if (i-j >= 0):
                temp += hn[j]*y[i-j]
        yp.append(temp)
    return yp


op = fmag(k)
plt.plot(op, color='red')
plt.show()
