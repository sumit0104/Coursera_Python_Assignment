#Sumit Gupta
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
l=[]
tags = soup('a')
for tag in tags:
    l.append(tag.get('href', None))
count=int(input("count: "))-1
position=int(input("position: "))-1
while(count):
    url = l[position]
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    l=[]
    tags = soup('a')
    for tag in tags:
        l.append(tag.get('href', None))
    count-=1
print(l[position])



# Enter - http://py4e-data.dr-chuck.net/known_by_Azedine.html
# count: 7
# position: 18
# http://py4e-data.dr-chuck.net/known_by_Atlanta.html
