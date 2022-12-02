import numpy as np
f = open('input','r')

l=[]
for i in f:
    l.append([9,*i[:-1],9])
l=[[9]*len(l[0])]+l+[[9]*len(l[0])]
l=np.array([[int(i) for i in j] for j in l])

def n(l,p):
    a=[]
    x,y=p
    if 0<x:
        a.append((x-1,y))
    if 0<y:
        a.append((x,y-1))
    if x<len(l):
        a.append((x+1,y))
    if y<len(l[0]):
        a.append((x,y+1))
    return a

a=[]
for x in range(1,len(l)-1):
    for y in range(1,len(l[0])-1):        
        if l[x][y]<min([l[i]for i in n(l,(x,y))]):
            a.append((x,y))

def check(i,v):
    
    u={i}
    size=1

    while u:
        i=list(u)[0]
        u.remove(i)
        v.add(i)
        for j in n(l,i):
            if l[i]<l[j]<9 and j not in v.union(u):
                u.add(j)
                size+=1

    return size,v

v=set()
x=[]
for i in a:
    s,v=check(i,v)
    x=sorted(x+[s])[-3:]

print(np.prod(x))
