import re

'''
fname = input('Enter name:')
fh = open(fname)
for line in fh :
     line = line.rstrip()
     if re.search('^X.*:',line) :
         print(line)
'''

x = 'Hi, my favorite numbers are 3 and 26'
y = re.findall('[0-9]+',x)
print(y)

line = 'From nikhilcg@gmail.com Sun 04 12 2019'
y = re.findall('^From .*@([^ ]*)',line)
print(y)