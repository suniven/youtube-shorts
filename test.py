import re

a='43,567'
a=re.sub('(,)','',a)
print(a)

a='https://www.youtube.com/shorts/AUXSZtyAnGk'
print(a[-11:])