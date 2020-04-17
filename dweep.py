import dweepy as dp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
x = dp.get_latest_dweet_for('accel')
data = x[0]['content']['accx']
print(data)
k = data.split(sep=',')
k.pop(-1)
val = list(map(int, k))
N = 11
hdn = []
for i in range(-5, 6):
    a, b = quad(lambda w: np.cos(w*i) + 1j*np.sin(w*i), -1*np.pi/4, 1*np.pi/4)
    hdn.append(a/6.28)

print(hdn)


def fmag(y):
    yp = []
    for i in range(len(y)):
        temp = 0
        for j in range(len(hdn)):
            if (i-j >= 0):
                temp += hdn[j]*y[i-j]
        yp.append(temp)
    return yp


op = fmag(val)
plt.subplot(211)
plt.grid(True)
plt.plot(val)
plt.subplot(212)
plt.plot(op, color='red')
plt.show()
