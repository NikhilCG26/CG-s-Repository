file = open("D:/Python/UM - Coursera/RoughWork/text.txt",'r')
for line in file :
    line = line.rstrip()
    if line.startswith('Mr') :
        print(line)
    #print(line)
#print(file)
"""
inp = file.read()

pos = inp.find('the')
print(pos)
"""