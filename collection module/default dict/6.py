"""
Python defaultdict Type for Handling Missing Keys
Behind the scenes, defaultdict uses the special __missing__() method:

It is automatically called when a key is not found.
If a default_factory is provided: its return value is used.
If default_factory is None: a KeyError is raised.
"""

from collections import defaultdict
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2
print(d)

print(d.__missing__('x'))
print(d.__missing__('d'))
print(d['a'])     
print(d['z'])         # Normal access to existing key

