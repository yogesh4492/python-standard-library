import re
#its match object
text='hello jay ehat is 22 jay'


print(re.search('ja',text))

# there is three match object method 
#1. .span(): its return start and end

print(re.search("ja",text).span())

#2. .string : its return passes string if matched else attributeerror
x=re.search("ja",text)
print(x.string)


#3. .group() its only return mathed specified string
print(re.search("ja",text).group())
