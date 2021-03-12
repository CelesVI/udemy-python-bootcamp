import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
##print(tips.head())
##print(flights.head())
##tip2 = tips.corr()
##sns.heatmap(tip2, annot=True, linewidths=1)
##plt.show()
##flight2 = flights.corr()
##sns.heatmap(flight2, annot=True, linewidths=1)
##plt.show()

flight2 = flights.pivot('month','year','passengers')
sns.heatmap(flight2, annot=True,  fmt='d')
plt.show()
