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
h1 = []
'''for i in range(11):
    tmp = np.exp(-1j*5*2*np.pi*i/11)
    h1.append(tmp)
# print(h1)'''
for i in range(8):
    if(i <= 3):
        tmp = np.exp((-1j*7*2*np.pi*i)/15)
        h1.append(tmp)
    elif (i == 4):
        tmp = 0.4*np.exp((-1j*7*2*np.pi*i)/15)
        h1.append(tmp)
    else:
        h1.append(0)
print(h1)
hn = []
for i in range(15):
    tmp = h1[0]
    for j in range(1, 8):
        tmp += 2*np.real(h1[j]*np.exp((1j*2*np.pi*j*i)/15))
    hn.append(tmp/15)
print(hn)


"""def fmag(y):
    yp = []
    for i in range(len(y)):
        temp = 0
        for j in range(len(hn)):
            if (i-j >= 0):
                temp += hn[j]*y[i-j]
        yp.append(temp)
    return yp


op = fmag(k)

# plt.subplot(211)
plt.grid(True)
# plt.plot(k)
# plt.subplot(212)
plt.plot(op, color='red')
plt.show()"""
print(np.exp(-1j*7*2*np.pi*2/15))
