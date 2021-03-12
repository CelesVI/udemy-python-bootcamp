import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
sns.countplot(x='smoker', data=tips)
sns.despine()
sns.set_style('darkgrid')
plt.show()
