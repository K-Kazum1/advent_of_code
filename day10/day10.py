f=open('input','r')

c={')':3,']':57,'}':1197,'>':25137}
d={'(':')','[':']','{':'}','<':'>'}



def check(x,p=''):
    if x=='':
        return 0
    if p=='':
        return check(x[1:],x[0])
    if x[0] in d:
        return check(x[1:],p+x[:1])
    elif x[0]!=d[p[-1]]:
        return c[x[0]]
    return check(x[1:],p[:-1])

s=0
for i in f:
    s+=check(i[:-1],'')

    print(s)
