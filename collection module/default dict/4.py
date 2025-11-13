"""using str as defaultdict """
from collections import defaultdict

# Using str as the factory function
sd = defaultdict(str)
sd['greeting'] = 'Hello'
print(sd)
#repr method that match the 
print(repr(sd['name']))

