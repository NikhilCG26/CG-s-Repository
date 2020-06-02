"""
fruit = 'banana'
for letter in fruit :
    print(letter)

index = 0
while index < len(fruit) :
    letter = fruit[index]
    print(letter)
    index = index + 1
"""
"""
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)

for i in range(1,count) :
    print(i)
"""

w = 'There'
print('hello'.upper(),w.lower(),'hi',w.upper())

print('hello'+w+'hi')

fruit = 'banana'
pos = fruit.find('d')
print(pos)

str = 'hello world'
change = str.replace('world','nikhil')
print(change)