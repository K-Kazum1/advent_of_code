import re

d ={'/':{}}
cur=[]

def traverse(a,b):
    if b:
        return traverse(a[b[0]],b[1:])
    return a

for i in open('data','r'):
    i=i[:-1]
    if i[2:4]=='cd':
        if i[-1]=='.':
            cur.pop()
        else:
            cur.append(i[5:])
    elif a:=re.match('(\d+) (.+)',i):
        traverse(d,cur)[a[2]]=int(a[1])

    elif a:=re.match('dir (.+)',i):
        traverse(d,cur)[a[1]]={}
e=[]

def size(a):
    return sum(a[i] if isinstance(a[i],int) else size(a[i]) for i in a)


def trav(cur):
    a = traverse(d,cur)
    if isinstance(a,int):
            return a

    g = sum(trav(cur+[i]) for i in a)
    e.append(g)
    
    return g
        
trav(['/'])
print(sum(i for i in e if i<=100000))
print(sorted([i for i in e if i+40000000>size(d)])[0])
