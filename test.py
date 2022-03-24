import re

a='43,567'
a=re.sub('(,)','',a)
print(a)