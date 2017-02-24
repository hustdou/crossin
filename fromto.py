import re
with open('from.txt','r') as f:
    str = f.read()
m = re.findall(r'\b[A-z]+\b',str)
m.sort()
f = open('to.txt','w')
for i in m:
    f.writelines(i+'\n')
f.close()