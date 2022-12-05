import re

s=[]
for i in open('data','r'):
    
    a = re.match('move (\d+) from (\d+) to (\d+)',i)
    if a:
        ss = []
        for i in range(int(a[1])):
            ss+=s[int(a[2])-1].pop(0)
        s[int(a[3])-1] = ss+s[int(a[3])-1]
        
    else:
        
        if not s:
            s = [[] for j in range(len(i)//4)]

        for j in range(len(i)//4):
            if i[j*4+1] != ' ':
                s[j].append(i[j*4+1])

print(''.join([i[0] for i in s]))
        

            

    

    
