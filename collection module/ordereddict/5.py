"""Reversing the order """
from collections import OrderedDict

d1 = OrderedDict([('a', 1), ('c', 2), ('b', 3)])
d2 = OrderedDict(reversed(list(d1.items())))


for k, v in d2.items():
    print(k, v)