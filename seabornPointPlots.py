import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

diamond = sns.load_dataset('diamonds')

sns.distplot(diamond['price'], kde=False)
##sns.rugplot(diamond['price'])
##sns.kdeplot(diamond['price'])
plt.show()
##plt.show() #Idem matplotlab para mostrar los plot. No olvidarse de import matplotlib.pyplot

