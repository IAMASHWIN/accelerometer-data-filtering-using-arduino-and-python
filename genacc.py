import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x = []
for i in range(20):
    x.append(-20)
    x.append(20)
for i in range(10):
    x.append(-20)
    x.append(-19)
    x.append(20)
    x.append(21)
#x = np.random.randint(-20, 20, 100,)
plt.plot(x)
t = pd.DataFrame(x)
print((t))
t.to_csv('data1.csv')
plt.show()
