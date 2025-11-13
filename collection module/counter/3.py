from collections import Counter
ctr = Counter([1, 2, 2, 3, 3, 3])
items = list(ctr.elements())

# print(items)


items=tuple(ctr.elements())
print(items)

ctr={'jay':1,'om':2,'krishna':3,'ram':4}
print(sorted([1,2,3,10,4,5]))

ctr={'ram':34,'namm':37}

print(ctr)

jay=[f for f in range(1,100)]
print(jay)