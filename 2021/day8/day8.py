f = open('input','r')

l=[0]*9
for i in f:
    for j in i[i.index('|')+2:-1].split(' '):
        l[len(j)]+=1
print(l[2]+l[3]+l[4]+l[7])
