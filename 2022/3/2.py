s=0

c=[]

for i in open('data','r'):
    c.append(set(i[:-1]))
    if len(c)==3:
        a = [j for j in i if all([j in k for k in c])][0]
        if a.isupper():
            s +=ord(a)-ord('A')+27
        else:
            s +=ord(a)-ord('a')+1
        c=[]
        print(s)


    
