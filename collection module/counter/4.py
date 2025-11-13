from collections import Counter
ctr = Counter([1, 2, 2, 3, 3, 3])
common = ctr.most_common(1) # means it give all that repeat the value 1 time
print(common)


l1=['yogesh','ram','shyam','yogesh']
com=Counter(l1)
print(com)