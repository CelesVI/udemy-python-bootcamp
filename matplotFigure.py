import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(0,10,20)
y = x * x
z = x + y

##plt.plot(x,y)

fig = plt.figure(figsize = (20,20))
axes = fig.add_axes((0,0,1,1))
axes.plot(x,y)
##x1 = fig.add_axes([0.1,0.1,0.8,0.8])
##x1.plot(x,y)
##x2 = fig.add_axes([0.4,0.4,0.3,0.3])
##x2.plot(y,x)

fig, axes = plt.subplots(2,1, figsize=(5,5))
axes[0].plot(x,y, marker = 'o', markersize= 10, markerfacecolor= 'red')
axes[1].plot(y,x)
##plt.tight_layout()
plt.show()
