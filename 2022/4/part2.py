
a =0
ran = lambda a,b:range(a,b+1)

for i in open('data','r'):
    i = [set(ran(*[int(jj) for jj in j.split('-')])) for j in i.split(',')]
    j = set.intersection(*i)

    if j:
        a+=1
print(a)
