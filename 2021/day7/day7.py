import numpy as np
f = open('input','r')
a=np.array([int(i) for i in f.readline().split(',')])

print(min([abs(a-i).sum() for i in a]))
