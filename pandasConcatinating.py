import numpy as np
import pandas as pd

x1 = {'a':[1,2,3,4,5],'b':[1,2,3,4,5],'c':[1,2,3,4,5],'d':[1,2,3,4,5],'e':[1,2,3,4,5]}
x2 = {'a':[2,3,4,5,6],'b':[2,3,4,5,6],'c':[2,3,4,5,6],'d':[2,3,4,5,6],'e':[2,3,4,5,6]}
x3 = {'a':[3,4,5,6,7],'b':[2,3,4,5,7],'c':[3,4,5,6,7],'d':[3,4,5,6,7],'e':[3,4,5,6,7]}

df1 = pd.DataFrame(x1, index=[1,2,3,4,5])
df2 = pd.DataFrame(x2, index=[1,2,3,4,5])
df3 = pd.DataFrame(x3, index=[1,2,3,4,5])

#print(df1, sep='\n')
#print(df2, sep='\n')
#print(df3, sep='\n')

print(pd.concat((df1,df2), axis = 1))