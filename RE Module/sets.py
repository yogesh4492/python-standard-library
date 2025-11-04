import re

# [arn] its retun if match a,r or n

text="Hello How are you my  01:45 44 35 name is yogesH"

print(re.findall('[arn]',text))

#[a-z] its return if lower abcd
print(re.findall('[a-z]',text))


# [^arn] its retun if not match a,r,n

print(re.findall('[^arn]',text))


#[0-9][0-9] its match data if 00 from 99 if in two digit combination no 1,2 match 01 ,02 match

print(re.findall('[0-9][0-9]',text))


