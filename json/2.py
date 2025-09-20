import json
import csv

""" Json Dump Is used to change or insert data in  a json data file"""

data={"name":"ram","age":25,"skills":"pyhton"}

with open("2.json",'w') as j:
    json.dump(data,j)
    json.dump(data,j,indent=4)#formatting
    json.dump(data,j,indent=4,sort_keys=True)#sort by alphabet 
    json.dump(data,j,indent=4,separators=(",",":"))#de fefault its same




""" use sort key ]sor t indent for roirmat json
encoding utf for special character avoid 
json.jsondecodeerror """