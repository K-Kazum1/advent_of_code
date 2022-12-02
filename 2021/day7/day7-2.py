import numpy as np
f = open('input','r')
a=np.array([int(i) for i in f.readline().split(',')])

print(min([(lambda x:np.abs(x*(np.abs(x)+1)/2))(a-i).sum() for i in a]))
