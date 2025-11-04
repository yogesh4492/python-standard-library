import re
p=re.compile('\w')
print(p.findall("he said * in 20025"))

p=re.compile('\w+')
print(p.findall("he said * in 2025"))

p=re.compile('\W')
print(p.findall("he said * in 2025"))
