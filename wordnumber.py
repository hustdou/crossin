# coding: utf-8
import re
with open('wordnumber.txt','r') as f:
    content = f.read()
wordlist = re.findall(r'\b\w+\b',content)
number = len(wordlist)
print number