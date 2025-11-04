import re
pattern ="\d+"
text = "Hello World 90"
match = re.match(pattern, text)
print(match)
if match:
    print("Match found:", pattern)
else:
    print("Match Not Found")

# re.match()