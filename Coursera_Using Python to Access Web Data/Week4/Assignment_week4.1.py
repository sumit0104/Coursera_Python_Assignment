#Sumit Gupta
#  We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#
#     Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#     Actual data: http://py4e-data.dr-chuck.net/comments_257178.html (Sum ends with 7)
#
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
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
tags = soup('span')
for tag in tags:
    l.append(int(tag.contents[0]))
print(sum(l))



# Enter -  http://py4e-data.dr-chuck.net/comments_257178.html
# 2407
