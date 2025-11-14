from collections import defaultdict

list1=[109,30,45,33]

d=defaultdict(list)

for i in range(len(list1)):
    d[i] = list1[i]

print(d)