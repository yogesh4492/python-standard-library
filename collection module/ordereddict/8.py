""" delete and reinsering """

from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
od.pop('c')    # Delete 'c'

for k, v in od.items():
    print(k, v)

od['c'] = 3    # Re-insert 'c' at end
for k, v in od.items():
    print(k, v)