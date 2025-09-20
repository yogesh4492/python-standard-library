"""json : Javascript Nottion Object """
""" Ligth weight data communication"""

"""load method to get data from json file ex json file  is 1.josn"""

import json
import csv

with open("./1.json",'r') as j:
    data=json.load(j)
    print(data)
    fields=list(data.keys())

with open("1.csv","w") as c:
    csw=csv.DictWriter(c,fieldnames=fields)
    csw.writeheader()
    row={k:data[k] for k in data}
    csw.writerow(row)