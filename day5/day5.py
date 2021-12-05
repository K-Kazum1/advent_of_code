f = open('input','r')
import re
import numpy as np
table=np.zeros((1000,1000))

for i in f:
    x=re.match('([\d]+),([\d]+) -> ([\d]+),([\d]+)',i)
    x0,x1,x2,x3=int(x[1]),int(x[2]),int(x[3]),int(x[4])

    if x0==x2:
        if x1>x3:
            x1,x3=x3,x1
        for j in range(x1,x3+1):
            table[x0][j]+=1
    if x1==x3:
        if x0>x2:
            x0,x2=x2,x0
        for j in range(x0,x2+1):
            table[j][x1]+=1
print(np.where(table>1,1,0).sum())
