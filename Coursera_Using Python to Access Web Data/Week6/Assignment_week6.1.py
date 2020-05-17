#Sumit Gupta
#  We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#
#     Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#     Actual data: http://py4e-data.dr-chuck.net/comments_257181.json (Sum ends with 57)
#
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
import json
import urllib.request, urllib.parse, urllib.error
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
s=0
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    print('Retrieving',address)
    uh=urllib.request.urlopen(address)
    data=uh.read().decode()
    js= json.loads(data)
    length=len(js['comments'])
    for i in range(length):
        s+=js['comments'][i]['count']
    print(s)


# Enter location:  http://py4e-data.dr-chuck.net/comments_257181.json
# Retrieving  http://py4e-data.dr-chuck.net/comments_257181.json
# 2757
