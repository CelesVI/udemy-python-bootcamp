import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly as pl
import cufflinks as cf
import plotly.offline as po
po.init_notebook_mode(connected=True)
cf.go_offline()
df = pd.DataFrame(np.random.rand(100,5), columns=['a','b','c','d','e'])
df1 = pd.DataFrame({'x':['a','b','c','d','e'],'y':[1,2,5,4,5],'z':[5,6,4,2,9]})
df.plot(kind='scatter', x='a', y='b')
##df.scatter_matrix()
plt.show()
