f=open('input','r')

c={')':3,']':57,'}':1197,'>':25137}
d={'(':')','[':']','{':'}','<':'>'}
e={'(':1,'[':2,'{':3,'<':4}



def check(x,p=''):
    if x=='':
        return p
    if p=='':
        return check(x[1:],x[0])
    if x[0] in d:
        return check(x[1:],p+x[:1])
    elif x[0]!=d[p[-1]]:
        return ''
    return check(x[1:],p[:-1])

s=0
t=[]
for i in f:
    s=check(i[:-1],'')

    if s:
        f=0
        for j in s[::-1]:
            f=5*f+e[j]
        t.append(f)

print(sorted(t)[len(t)//2])



    
