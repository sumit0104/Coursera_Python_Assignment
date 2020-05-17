# Sumit Gupta
import re
fh=open(input())
l=[]#list for collecting all numbers
for i in fh:
    lst=re.findall('[0-9]+',i)
    if len(lst)<1:
        continue
    else:
        for i in lst:
            l.append(int(i))
print(sum(l))


# regex_sum_257176.txt
# 384417
