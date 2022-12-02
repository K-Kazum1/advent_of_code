a ={'X':0,'Y':1,'Z':2,'A':0,'B':1,'C':2}
score = 0
for i in open('data','r'):
    i = [i[0],i[2]]

    if i[1]=='X':
        i[0] =[3,1,2][a[i[0]]]
    if i[1]=='Y':
        i[0] =[1,2,3][a[i[0]]]
    if i[1]=='Z':
        i[0] =[2,3,1][a[i[0]]]
    
    score +=(i[0]+3*a[i[1]])

print(score)
