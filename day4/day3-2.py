f = open('input','r')
import numpy as np

numbers=[int(i) for i in f.readline().split(',')]
f.readline()
bingos=[]

while True:
    bingos.append([])
    for i in range(5):
    bingos[-1].append([int(j) for j in f.readline()[:-1].split(' ') if j])
    if f.readline()=='':
        break

bingos = np.array(bingos)

def check(a):
    n=i=0
    while i<len(a):
        for ii in a[i]:
            if not any(ii):
                n=a[i].sum()
                a=np.delete(a,i,0)
                i-=1
        for ii in a[i].T:
            if not any(ii):
                n=a[i].sum()
                a=np.delete(a,i,0)
                i-=1
        i+=1
    return a,n

for i in numbers:
    bingos = np.where(bingos==i,0,bingos)
    bingos,s = check(bingos)

    if s!=0:
        print(s,i)
    
    
