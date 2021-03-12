import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly as pl
import cufflinks as cf
import plotly.offline as po
po.init_notebook_mode(connected=True)
cf.go_offline()
df = pd.DataFrame(np.random.rand(100,5), columns=['a','b','c','d','e'])
df1 = pd.DataFrame({'x':[3,4,7,8,12],'y':[1,2,5,4,5],'z':[5,6,4,2,9]})
##cf.datagen.sinwave(10,5)
df1.iplot(kind='surface')
plt.show()
