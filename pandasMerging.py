import numpy as np
import pandas as pd

df1 = pd.DataFrame({'key1':[1,2,3], 'a':[2,3,4], 'b':[3,4,5]})
df2 = pd.DataFrame({'key1':[1,2,3], 'a':[1,2,3], 'b':[3,4,6]})

df1.add(df2, fill_value=0)
print(df1)

#df1['c'] = df1['a'] + df1['b']
#print(df1)
#how misma lógica que cruzar tablas db.
#print(pd.merge(df1, df2, how='left', on='key1'))
