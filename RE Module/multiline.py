import re

text="""
hello jay
ell ness its
ello ness
"""
print(re.findall("^ello",text,re.MULTILINE))
print(re.findall("^ello",text,re.M))