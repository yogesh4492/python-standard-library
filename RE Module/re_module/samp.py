import re

s="geeksforgeeks : a computer science portal for geeks"
match=re.search(r'portal',s)
print(match.start())
print(match.end())
