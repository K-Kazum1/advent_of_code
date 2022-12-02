f = open('data','r')

l = []

a=0
for i in f:
    i=i[:-1]
    if i == '':
        l.append(a)
        a=0
    else:
        a+=int(i)

print(sum(sorted(l)[-3:]))
