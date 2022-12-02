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
    for i in a:
        for ii in i:
            if not any(ii):
                return i.sum()
        for ii in i.T:
            if not any(ii):
                return i.sum()
    return 0
d=0
for i in numbers:
    bingos = np.where(bingos==i,0,bingos)
    b = check(bingos)
    if b:
        break

print(i*b.sum())
