# from collections import Counter
# ctr1 = Counter([1, 2, 2, 3, 3, 3]) # From a list
# ctr2 = Counter({1: 2, 2: 3, 3: 1}) #  key value not  same because if key value same it remoe dupicate
# ctr3 = Counter('hellogood morning ') # From a string

# print(ctr1)
# print(ctr2)
# print(ctr3)
import typer
from collections import Counter
ctr = Counter(['jay', 2,'om', 3, 3, 3])

# Accessing count of an element
print(ctr[1])  
print(ctr[2])  
print(ctr[3])
print(ctr['om'])# it give how many time value appear in the list or iterable

