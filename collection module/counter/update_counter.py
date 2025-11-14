from collections import Counter

list1=[10,20,30,10,20,30]

co=Counter(list1)

print(co)

co.update([10,20])# pass iterable
print(co)



