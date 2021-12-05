f = open('input','r')

h=[0,0,0,0,0]
l=[0,0,0,0,0]

for i in f:
    i=i[:-1]

    for j in range(len(i)):
        if i[j]=='0':
            l[j]+=1
        else:
            h[j]+=1
print(h,l)

z=0
for j in range(len(h)):
    if l[j]<h[j]:
        z=2*z+1
    else:
        z*=2
       
print(z*(2**5-z-1))        
