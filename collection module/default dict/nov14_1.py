from collections import defaultdict



co=defaultdict(list)
co['juice'].append('mango')
co['vegitable'].append('apple')
print(co)

print(co['fruit'])# not give keyerror