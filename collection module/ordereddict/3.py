"""changing value does not affect order"""

from collections import OrderedDict

od = OrderedDict([('d', 1), ('b', 2), ('a', 3), ('c', 4)])
od['c'] = 5  

for k, v in od.items():
    print(k, v)