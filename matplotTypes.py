import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1,2,3,4,5]
y = [i*i for i in range(len(x))]
print(y)

##plt.scatter(x,y)
##plt.fill(x,y, color='red')
##plt.bar(x,y)

plt.subplot(2,2,1)
plt.scatter(x,y)
plt.subplot(2,2,2)
plt.hist(x,y)
plt.subplot(2,2,3)
plt.bar(x,y)
plt.subplot(2,2,4)
plt.fill(x,y)
plt.subplot(2,2,4)
plt.polar(x,y)

plt.show()
