fname = input('Enter Name: ')
fh = open(fname)
email = []
for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') :
        #print('hi')
        continue
    words = line.split()
    email.append(words[1])
for i in email :
    print(i)
print('There were', len(email), 'lines in the file with From as the first word')
