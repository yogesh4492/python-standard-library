from collections import Counter

list=[10,20,30,40,10,20,30,10]

co=Counter(list)

print(co.most_common(2))# it print first two value appear most times in list or iterable

print(co)

