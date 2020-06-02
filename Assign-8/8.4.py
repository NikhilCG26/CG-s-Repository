inp = input('Enter Name: ')
ent = open(inp)
total = []
for line in ent :
    line = line.rstrip()
    words = line.split()
    for i in words :
        if i not in total :
            total.append(i)
total.sort()
print(total)
