freq={}

data=[1,2,1,3,4,3,2]

for i in data:
    freq[i]=freq.get(i,0)+1
# for j in data:
#     freq[i]=freq.get(i,0)+1
print(freq)