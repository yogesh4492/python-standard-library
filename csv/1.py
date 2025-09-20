import csv
import json

""" Read a csv files 
Twoi Main Way for read  
1) csv.reader()
2)csv.DictReader


"""
def read(file):
    with  open("1.csv",'r') as c:
    # d=csv.reader(c)
    # print(list(d))
    # for i in d:
    #     print(i)
        d1=csv.DictReader(c)
    # print(list(d1))
    # for i in d1
        return d1
    # print(list(d1['Age']))
    #     print(i['Age'])
    #     return i['Age']
# with open()
# with open("1.csv","r") as c1:
#     d1=csv.DictReader(c)
#     print(d1)
