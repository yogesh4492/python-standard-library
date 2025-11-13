"""equality check in order """

from collections import OrderedDict

od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('c', 3), ('b', 2), ('a', 1)])

print(od1 == od2)