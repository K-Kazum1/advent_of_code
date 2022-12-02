f=open('input','r')
l={}
x=y=0
for i in f:
    
    i=i[:-1]
    for x in range(len(i)):
        l[x,y] = int(i[x])
    y+=1
print(l)
import numpy as np
c=0

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
    if max(m.values())>9:
        m,a=tick(m,a)
    m={i:m[i] if m[i]>-1 else 0 for i in m}
    return m,a
s=0
for i in range(1,101):
    l,a=tick({i:l[i]+1 for i in l})
    s+=a
                    

    if i%10==0:
        print(np.array([[l[i,j] for i in range(x+1)] for j in range(y)]),s)
    
    
    
