import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tries = input('Enter the count:')
tries = int(tries)
pos = input('Enter position:')
pos = int(pos)
print(url)

for i in range(tries) :
    tags = soup('a')
    flag = 0
    for tag in tags :
        flag = flag + 1
        if flag != pos :
            continue
        else :
            link = tag.get('href', None)
            print(link)
            html = urllib.request.urlopen(link, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            
            
        # print(tag.get('href', None))