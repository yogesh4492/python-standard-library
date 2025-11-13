""" default dict is most use in real word its take the and does not get the keyerror and generate default key or new key"""

from collections import defaultdict
d=defaultdict(list)

d['fruites'].append('apple')
d['vegitable'].append('patato')
print(d)
print(d['juice'])
print(d['fruites'])
