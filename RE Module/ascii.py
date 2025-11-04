import re
#math only ascii values
text="hello how are you"
print(re.findall(r"\w",text,re.ASCII))