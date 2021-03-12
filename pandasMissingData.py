import numpy as np
import pandas as pd

d = {'a':[1,2,3,4,5], 'b':[6,7,8,9,np.nan], 'c':[0,1,2,np.nan,np.nan], 'd':[3,4,np.nan,np.nan,np.nan], 'e':[5,np.nan,np.nan,np.nan,np.nan]}
print(d)

df = pd.DataFrame(d)

#print(df)

#print(df.dropna(thresh = 3))

print(df['c'].fillna(value = df['b'].mean()))