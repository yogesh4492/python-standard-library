""" pop the last or first element """
from collections import OrderedDict
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

res = d.popitem(last=False)#remove first
res=d.popitem(last=True)# Remove last inserted item
print(res)
