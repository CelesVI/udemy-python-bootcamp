import matplotlib.pylab as plt
import seaborn as sns
import numpy as np

plt.figure("Test Plots")
lst1 = list(np.random.rand(10))
lst2 = list(np.random.rand(10))
sns.distplot(lst1, label='test_label1', color="0.25")
sns.distplot(lst2, label='test_label2', color="0.25")

plt.show()
