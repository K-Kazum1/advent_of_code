a ={'X':0,'Y':1,'Z':2,'A':0,'B':1,'C':2}
b=[3,0,6]
score = 0
for i in open('data','r'):
    i = [a[i[0]],a[i[2]]]    
    score += i[1]+1+ b[(i[0]-i[1])]

print(score)
