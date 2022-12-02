f=open('input','r')
import numpy as np

xs,ys=[],[]

for i in f:
    if i=='\n':
        break
    i=i[:-1]
    x,y=map(int,i.split(','))
    xs.append(x)
    ys.append(y)
        
l=np.zeros((max(xs)+1,max(ys)+1))
l[xs,ys]=1

for i in f:
    z,n=i[:-1].split('=')
    z,n=z[-1:],int(n)

    if z=='y':
        l=l.transpose()
    
    l=l[:n] + l[n+1:][::-1]

    if z=='y':
        l=l.transpose()
    
print((l>0).sum())

for i in l.transpose():
	print(''.join(['█' if j>0 else ' ' for j in i]))

    
