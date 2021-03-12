import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
##diamond =sns.load_dataset('diamonds')
##print(tips)
x = sns.pairplot(tips, hue='day')
x.map_diag(sns.distplot)
x.map_lower(sns.kdeplot)
plt.show()
