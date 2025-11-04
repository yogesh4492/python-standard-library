import re

#print also case insentive and if not available in string
text="hello How are You my name is yogesh"
print(re.findall("hello",text,re.DEBUG))
print(re.findall("jay",text,re.DEBUG))