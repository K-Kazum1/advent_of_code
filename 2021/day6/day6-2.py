f = open('input','r')
f=f.readline()

a=[int(i) for i in f.split(',')])
a={i:a.count(i) for i in range(9)}

for i in range(256):
    b={i:0 for i in range(9)}
    for j in range(9):
        if 0<j:
            b[j-1]+=a[j]
        else:
            b[8]+=a[0]
            b[6]+=a[0]            
    a=b
            
print(sum(a[i] for i in a))
