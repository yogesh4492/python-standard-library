import re
#its replace the string whith another string
text = "apple banana apple"
new_text = re.sub(r"apple", "orange", text)
print(new_text)
#same as string replace method
new=text.replace('apple','orange')
print(new)
