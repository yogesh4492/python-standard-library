from collections import Counter

list1=[1,2,3,4,1,2,4,3,5,6,6,5,7,8,9]

co=Counter(list1)
print(co)
print(list(co.elements()))

