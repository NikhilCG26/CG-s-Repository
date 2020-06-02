import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = input('Enter -')
sauce = urllib.request.urlopen(url).read()
soup = BeautifulSoup(sauce, 'html.parser')
print(soup)
#Retrieve all of the anchor tabs
tags = soup('a')
for tag in tags :
    print(tag.get('href', None))