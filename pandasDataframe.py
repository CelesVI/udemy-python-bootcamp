import numpy as np
import pandas as pd

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,0,1,2]
d = [3,4,5,6]
e = [7,8,9,0]

a1 = [4,2,0,4]
b1 = [7,2,7,8]
c1 = [9,4,1,6]
d1 = [3,9,5,6]
e1 = [4,8,5,0]

df = pd.DataFrame([a,b,c,d,e],['a','b','c','d','e'],['W','X','Y','Z'])
df1 = pd.DataFrame([a1,b1,c1,d1,e1],['a','b','c','d','e'],['W','X','Y','Z'])

df.drop('W', axis = 1)

#print(df.iloc['a', 'Y'])

print((df['W'] > 3) & (df['Z']> 2))

