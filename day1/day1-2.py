f=open('input','r')

c=0
j=[]
r=9999
for i in f:

    i=int(i)

    j.append(i)
    if len(j)==4:
        j.pop(0)

        if r<sum(j):
            c+=1
        r=sum(j)
    
print(c)
