import re

s=[]
for i in open('data','r'):
    if a:=re.match('move (\d+) from (\d+) to (\d+)',i):
        print(s)
        for i in range(int(a[1])):
            s[int(a[3])-1].append(s[int(a[2])-1].pop())        
    else:        
        if not s:
            s = [[] for j in range(len(i)//4)]

        for j in range(1,len(i),4):
            if i[j] != ' ':
                s[j//4].insert(0,i[j])

print(''.join([i[-1] for i in s]))
        

            

    

    
