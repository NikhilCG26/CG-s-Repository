name = input('Enter Name: ')
fh  = open(name)
count = dict()
for line in fh :
    if line.startswith('From:') :
        words = line.split()
        if words[1] not in count :
            count[words[1]] = 1
        else :
            count[words[1]]  = count[words[1]] + 1

bigword = None
bignum = None
for k,v in count.items() :
    if bignum is None or v > bignum :
        bignum = v
        bigword = k
print(bigword,bignum)

    
        