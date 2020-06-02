import urllib.error, urllib.parse, urllib.request
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = input('Enter-')
sauce = urllib.request.urlopen(fhand, context=ctx)
data = sauce.read().decode()
info = json.loads(data)

total = 0
count = 0
comment = info["comments"]
for item in comment :
    val = item["count"]
    total = total + int(val)
    count = count + 1
print('Sum: ', total)
print('Count: ',count)
