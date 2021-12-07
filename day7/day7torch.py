import torch
from torch import nn
import torch.optim as optim
f = open('input','r')
a=torch.tensor([int(i) for i in f.readline().split(',')])
b=nn.parameter.Parameter(torch.zeros(1))
optimizer = optim.RMSprop([b], lr=0.001)

loss = lambda x:((x**2+x)/2).sum()
                         
for i in range(10000):
    optimizer.zero_grad()
    loss((a-b).abs()).backward()
    optimizer.step()
print(loss((a-b).abs()).item())
