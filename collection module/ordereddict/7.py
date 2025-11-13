""" Move key font to end"""

from collections import OrderedDict
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

d.move_to_end('a')         # Move 'a' to end
d.move_to_end('b', last=False)  # Move 'b' to front

for k, v in d.items():
    print(k, v)