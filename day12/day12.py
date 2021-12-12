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


def f(h,v):
    c=0        
    for i in d[h]:
        if i not in v:
            if i=='end':
                c+=1
                #print(','.join(v))
            else:
                c+=f(i,v+[i.lower()])
    return c

print(f('start',['start']))
