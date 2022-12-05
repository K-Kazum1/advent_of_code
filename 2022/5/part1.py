import re

s=[]
for i in open('data','r'):
    if a:=re.match('move (\d+) from (\d+) to (\d+)',i):
        for i in range(int(a[1])):
            s[int(a[3])-1].insert(0,s[int(a[2])-1].pop(0))        
    else:        
        if not s:
            s = [[] for j in range(len(i)//4)]

        for j in range(1,len(i),4):
            if i[j] != ' ':
                s[j//4].append(i[j])

print(''.join([i[0] for i in s]))
        

            

    

    
