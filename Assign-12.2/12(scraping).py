# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total = 0
count = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    #print(type(tag))
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    y = str(tag)
    value = re.findall("[0-9]+",y)
    for i in value :
        i = int(i)
        total = total + i
        count = count + 1
    #value = tag.get('class=')
    #print(value)
print('Sum = ',total)
print('Count = ',count)
