from collections import Counter

list1=[1,2,3,4,5,5]
print(list1)


cou=Counter(list1)# count frequency how many times the value appear in list or any iterable  
print(cou)

print(cou[5])# it printhow many time 5 appear in list or any iterable
print(cou['6'])# its not give keyerror its main advantage of collection 

