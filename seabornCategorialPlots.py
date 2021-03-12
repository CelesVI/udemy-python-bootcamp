import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

##sns.pointplot(x='total_bill', y='day', data=tips, kind='box')
##sns.swarmplot(x='total_bill', y='day', data=tips, hue='sex', palette='magma')
##sns.stripplot(x='total_bill', y='day', data=tips, hue='sex', palette='magma')
##sns.barplot(x='day', y='tip', data=tips, hue='sex')
sns.violinplot(x='day', y='tip', data=tips, hue='sex')

plt.show()
