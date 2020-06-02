#t = input('D:/Python/UM - Coursera/RoughWork/text.txt')
file = open('D:/Python/UM - Coursera/RoughWork/text.txt','r')
print(file)

inp = file.read()
"""
if inp.lower() == 'potter'.lower() :
    print('hi')
print(len(inp))
print(inp[:20])
"""
pos = inp.find('Potter')
print(pos)
count = 0
for i in inp :
    i = i.rstrip()
   # if i.startswith('Mr') :
    print(i)
print(count)
