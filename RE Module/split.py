import re
#separate the string by some separator like ',(comma),;(semicolon)'
text = "one,two;three four"
parts = re.split(r"[,; ]+", text)
print(parts)  # ['one', 'two', 'three', 'four']