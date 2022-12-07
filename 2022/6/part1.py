

a = open('data','r').readline()

for i in range(len(a)):
    if len(set(a[i:i+4]))==4:
        break

print(i+4)

