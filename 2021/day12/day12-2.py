f = open('input','r')

d={}

for i in f:
    i=i[:-1]
    a,b=i.split('-')

    if a in d:
        d[a].add(b)
    else:
        d[a]={b}

    if b in d:
        d[b].add(a)
    else:
        d[b]={a}


def f(h,v,b=[],t=0):
    c=0
    if h.islower():
        b=b+[h]
    for i in d[h]:
        bb=max(b.count(j) for j in b)==2 and i.islower()
        if i not in v and b.count(i)<2-bb:
            #print('\t'*t,h,i)
            
            if i=='end':
                c+=1
            else:
                c+=f(i,v+([i]if bb else []),b,t+1)
    return c


print(f('start',['start']))
