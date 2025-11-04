import re 
string =""" hello my number is 99999999999 and
            my friend number is 8888888888"""
regrex = '\d+'
match =re.findall(regrex,string)
print(match)
