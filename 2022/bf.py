def bf(c,s=False,p=0,v=False):
    c = ''.join([i for i in c if i in '<>+-[],.'])

    if not s:
        s = [0]
    stack = []

    a = 0
    while a < len(c):
        if v:
            try:
                print(c[:a]+'('+c[a]+')'+c[a+1:],[str(s[i]) if i== p else s[i] for i in range(len(s))])
            except:
                pass
        if c[a]=='+':
            s[p]+=1
        elif c[a]=='-':
            s[p]-=1
        elif c[a]=='>':
            p+=1
            if len(s)-1<p:
                s.append(0)
        elif c[a]=='<':
            p-=1
        elif c[a]=='[':
            if s[p]:
                stack.append(a)
            else:
                z = 1
                x=a+1
                while z:
                    if c[x]=='[':
                        z+=1
                    elif c[x]==']':
                        z-=1
                    x+=1
                a=x-1
        elif c[a]==']':
            if s[p]:
                a = stack[-1]
            else:
                stack.pop()
        elif c[a]==',':
            inp = input()
            if not inp:
                inp=0
            s[p] = int(inp)
        elif c[a]=='.':
            print(s[p])

        a+=1
    return s,p
                
                
            
    
