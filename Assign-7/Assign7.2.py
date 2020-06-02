fname = input('Enter File Name: ')
fh = open(fname,'r')
count = 0
add = 0
for line in fh :
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:") :
        pos = line.find(':')
        val = line[pos+1:]
        fval = float(val)
        add = add + fval
        count = count + 1  
    
avg = add/count
print('Average spam confidence:',avg)