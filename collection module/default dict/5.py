"""Groupping word by first character """

from collections import defaultdict
words = ["apple", "ant", "banana", "bat", "carrot", "cat"]
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)

print(grouped)