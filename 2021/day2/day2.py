f=open('tx2','r')

h=0
d=0

for i in f:
    j=int(i.split(' ')[-1])
    if i[0]=='f':
        h+=j
    if i[0]=='d':
        d+=j
    if i[0]=='u':
        d-=j
print(h*d)
