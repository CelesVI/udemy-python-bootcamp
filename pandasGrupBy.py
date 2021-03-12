import numpy as np
import pandas as pd

p = {'item':['apple','apple','orange','orange','grape','grape', 'bananas'], 'days':['mon','tue','wed','thu','fri','sat','sun'], 'sales':[100,80,200,100,5,10,15]}
#print(p)

df = pd.DataFrame(p)

x = df.groupby('item')

#print(x.mean())
#print(x.sum())
#print(x.std())
print(x.describe().transpose())