f=open('input','r')
import numpy as np
l={}
x=y=0
for i in f:
    
    i=i[:-1]
    for x in range(len(i)):
        l[x,y] = int(i[x])
    y+=1
l=np.array([[l[i,j] for i in range(x+1)] for j in range(y)])
print(l)
import numpy as np

def tick(l,a=0):
    m=l
    for i in range(x+1):
        for j in range(y):
            if l[i,j]>9:
                a+=1
                if 0<i:
                    if 0<j:
                        m[i-1,j-1]+=1
                    m[i-1,j]+=1
                    if j<x:
                        m[i-1,j+1]+=1
                if 0<j:
                    m[i,j-1]+=1
                m[i,j]=-9999
                if j<x:
                    m[i,j+1]+=1
                if i<x:
                    if 0<j:
                        m[i+1,j-1]+=1
                    m[i+1,j]+=1
                    if j<x:
                        m[i+1,j+1]+=1
    if m.max()>9:
        m,a=tick(m,a)
    m=np.where(m>-1,m,0)
    return m,a
s=0
i=0
while True:
    i+=1
    l,a=tick(l+1)
    s+=a
                    

    if i%10==0:
        print(l,s)
    if l.sum()==0:
        break
    
    
    
