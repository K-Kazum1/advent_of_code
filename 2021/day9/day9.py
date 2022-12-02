f = open('input','r')

l=[]

for i in f:
    i=i[:-1]
    l.append([9,*i,9])

l=[[9]*len(l[0])]+l+[[9]*len(l[0])]
l=[[int(i) for i in j] for j in l]

total=0
for x in range(1,len(l)-1):
    
    for y in range(1,len(l[0])-1):
        
        if l[x][y]<min(l[x-1][y],l[x+1][y],l[x][y-1],l[x][y+1]):
            print(l[x][y])
            total+=int(l[x][y])+1
