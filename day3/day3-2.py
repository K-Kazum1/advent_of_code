f = open('input','r')

q=[]

for i in f:
    i=i[:-1]
    q.append(i)
    
i=0
while len(q)>1:
    l=h=0
    for j in range(len(q)):
        if q[j][i]=='0':
            l+=1
        else:
            h+=1
    
    if h<l:#change this
        z=0
    else:
        z=1

    qq=[]
    for w in q:
        if w[i]!=str(z):
            qq.append(w)
    q=qq
    i+=1
print(q[0])#do this twice




    



    
