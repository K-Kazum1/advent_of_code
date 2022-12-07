

a = open('data','r').readline()

for i in range(len(a)):
    if len(set(a[i:i+14]))==14:
        break

print(i+14)

