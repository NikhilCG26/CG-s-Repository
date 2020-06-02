import xml.etree.ElementTree as ET
import urllib.error, urllib.parse, urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = input('Enter-')
sauce = urllib.request.urlopen(fhand, context=ctx)
data = sauce.read()
tree = ET.fromstring(data)
total = 0
count = 0
lst = tree.findall('comments/comment')
for i in lst :
    val = int(i.find('count').text)
    total = total + val
    count = count + 1
print('Count:',count) 
print('Sum:',total)
