import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
z = pd.read_csv('data.csv')
k = list(z['0'])
# hd(e^jω)=e^-jαω
# sample hd[ω] at N pts
# ω = 2*πk/N
# α=N-1/2
# h(ω)=e^-j(N-1/2)(2*πk/N)
hn = []
for i in range(15):
    temp = 1
    for j in range(1, 5):
        if j < 4:
            temp += 2*np.real(np.exp((-7j*2*np.pi*j+1j*2*np.pi*i*j)/15))
        else:
            temp += 2*np.real(0.4*np.exp(-56j*np.pi*j + 1j*2*np.pi*i*j)/15)
    hn.append(temp/15)
print(hn)
hn2 = []
for i in range(15):
    temp = 1
    for j in range(1, 4):
        temp += 2*np.cos(2*np.pi*j*(i-7)/15)
    temp += 0.8*np.cos(8*np.pi*(i-7)/15)
    hn2.append(temp/15)
print(hn2)
hn3 = []
for i in range(15):
    n = np.float(i-7)
    hn3.append((1+2*np.cos(2.00*np.pi*n/15)+2*np.cos(4.00*np.pi*n/15) +
                2*np.cos(6.00*np.pi*n/15)+0.8*np.cos(8.00*np.pi*n/15))/15)
print(hn3)


def fmag(y):
    yp = []
    for i in range(len(y)):
        temp = 0
        for j in range(len(hn3)):
            if (i-j >= 0):
                temp += hn3[j]*y[i-j]
        yp.append(temp)
    return yp


op = fmag(k)
plt.plot(op, color='red')
plt.grid(True)
plt.show()
