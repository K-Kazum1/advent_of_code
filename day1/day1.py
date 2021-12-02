
f=open('input','r')

j=9999
c=0
for i in f:
    i=int(i)
    if j<i:
        c+=1
    j=i
print(c)
