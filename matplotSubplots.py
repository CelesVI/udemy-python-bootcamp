import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y

plt.subplot(3,2,1)
plt.plot(x,x)
plt.subplot(3,2,2)
plt.plot(x,y)
plt.subplot(3,2,3)
plt.plot(x,z)
plt.subplot(3,2,4)
plt.plot(y,z)
plt.subplot(3,2,5)
plt.plot(z,x)
plt.subplot(3,2,6)
plt.plot(x,x)
plt.tight_layout()
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
