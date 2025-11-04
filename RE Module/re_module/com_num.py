import re
p=re.compile('\d')
print(p.findall("my name is yogesh my age is 20 my dob is 26-04-2005"))

p=re.compile('\d+')
print(p.findall("my name is yogesh my age is 20 my dob is 26-04-2005"))
