f=open('input','r')

h=0
d=0
a=0
for i in f:
    j=int(i.split(' ')[-1])
    if i[0]=='f':
        h+=j
        d+=a*j
    if i[0]=='d':
        
        a+=j
    if i[0]=='u':
        
        a-=j
    print(a,d,h)
print(h*d)


