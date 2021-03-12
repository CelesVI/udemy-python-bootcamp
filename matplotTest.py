import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y

plt.plot(x,y,x,x,z,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Graff')

plt.show()
