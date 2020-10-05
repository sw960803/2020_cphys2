import numpy as np
import pandas as pd

list_=[]
col=[]

for idx in range(1,10):
    col.append(str(idx)+' Times')
    for jdx in range(1,10):
        list_.append(str(jdx)+' x '+str(idx)+' = '+str(idx*jdx))

list_=np.array(list_)
list_=list_.reshape(9,9)
df=pd.DataFrame(list_,columns=col,index=range(1,10))

df