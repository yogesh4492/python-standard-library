import re

txt="hello how are you my name is yogesh patel"


# \A its return idf the specified character match at beggining"

print(re.findall("\Ahello",txt))

#\b its work with row string its check both side start and end from the specified value

txt1="hello yash how are you my name is yogesh"

print(re.findall(r"\byo",txt1))#from begining
print(re.findall(r"sh\b",txt1))# from ending


#\B it work if its placed only before starting if specified word(character) in center

print(re.findall(r'\Bo',txt1))
print(re.findall(r"s\B",txt1))

# \d for digit match,\d+ for digit as word \D non-digit match
# \w for character match,\w+ for word as word \D non-character match
# \s for whitespace match,\s+ for whitespace (two) as word \S non-Whitespace match


#\Z match specified string at the end

print(re.findall(r"esh\Z",txt1))
print(re.findall(r"esh\Z",txt))

