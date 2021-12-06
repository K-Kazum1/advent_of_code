f = open('input','r')

f=f.readline()
a=[int(i) for i in f.split(',')]

for i in range(18):
    b=[]
    for j in a:
        if 0<j:
            b.append(j-1)
        else:
            b.append(6)
            b.append(8)
    a=b

            
print(len(a))
