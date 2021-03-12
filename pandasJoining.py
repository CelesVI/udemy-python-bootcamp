import numpy as np
import pandas as pd

x1 = {'a':[1,2,3] , 'b':[5,6,7]}
y1 = {'c':[3,4,5] , 'd':[2,3,6]}

x = pd.DataFrame(x1 , index = ['p1','p2','p3'])
y = pd.DataFrame(y1 , index = ['p1','p2','p3'])

#print(x)
#print(y)
print(x.join(y)) 