f = open('input','r')

num='012346,01,02356,01235,0145,12345,123456,013,0123456,012345'.split(',')
t=0

for i in f:
    i=i[:-1]    
    
    nums=sorted([''.join(sorted(j)) for j in i[:i.index('|')-1].split(' ')],key=lambda x:len(x))
    l={j:[] for j in range(2,8)}
    for j in nums:
        l[len(j)].append(j)

    
    counts = {j:''.join([''.join(l[i]) for i in l]).count(j) for j in 'abcdefg'}
    
    x={}
    x['1'] = [i for i in 'abcdefg' if counts[i]==9][0]
    x['0'] = [i for i in l[2][0] if i!=x['1']][0]
    x['2'] = [i for i in 'abcdefg' if counts[i]==7 and not i in l[4][0]][0]
    x['3'] = [i for i in l[3][0] if i not in l[2][0]][0]
    x['4'] = [i for i in l[4][0] if counts[i]==6][0]
    x['5'] = [i for i in 'abcdefg' if counts[i]==7 and i in l[4][0]][0]
    x['6'] = [i for i in 'abcdefg' if i not in x.values()][0]
 

    cnum=[''.join(sorted(x[i] for i in j)) for j in num]
    s=0
    for j in i[i.index('|')+2:].split(' '):
        j = ''.join(sorted(j))
        s=s*10+cnum.index(j)
    
    t+=s
        
    
print(t)

            


