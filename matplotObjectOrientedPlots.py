import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y

##plt.plot(x,y)

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y,y,x)

plt.show()
