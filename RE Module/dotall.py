import re

text="""hello
my
name
is
yogesh
"""
# its match all the dotted include new line

print(re.findall('me.is',text,re.DOTALL))
print(re.findall('me.is',text,re.S))