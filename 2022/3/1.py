s=0

for i in open('data','r'):
    a = [j for j in i if j in set(i[len(i)//2:]) and j in set(i[:len(i)//2])][0]
    
    if a.isupper():
        s +=ord(a)-ord('A')+27
    else:
        s +=ord(a)-ord('a')+1
print(s)
    
