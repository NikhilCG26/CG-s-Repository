import re
fname = input('Enter Name: ')
fh = open(fname)

total = 0
count = 0
for line in fh :
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    #print(len(y))
    length = len(y)
    if length != 0 :
        for i in range(0,length) :
            total = total + int(y[i])
    count = count + len(y)
print('There are',count,'values and the sum is',total)