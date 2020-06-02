# Method 1:
'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
'''
'''
# Method 2: This gives the content without the headers
import urllib.request, urllib.error,urllib.parse

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page2.htm')
for line in fhand :
    print(line.decode().strip())
'''

import urllib.request, urllib.error,urllib.parse

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

count = dict()
for line in fhand :
    words = line.decode().split()
    for word in words :
        count[word] = count.get(word,0) + 1
print(count)