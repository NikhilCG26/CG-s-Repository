fname = input('Enter name:')
fh = open(fname)
for line in fh :
    line = line.rstrip()
    print(line.upper())