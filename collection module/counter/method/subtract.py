from collections import Counter

list=[1,2,3,42,1,2,3,43,67]
print(list)

co=Counter(list)
print(co)

co.subtract([2])
print(co)
