fname = input('Enter Name:')
fh = open(fname)
count = dict()
for line in fh :
    if line.startswith('From ') :
        words = line.split()
        #print(words)
        time = words[5].split(':')
        count[time[0]] = count.get(time[0],0) + 1
p = sorted([(k,v) for k,v in count.items()])
for k,v in p :
    print(k,v)
    
