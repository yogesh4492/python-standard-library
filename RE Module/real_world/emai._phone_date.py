import re

with open("sample.txt", "r") as f:
    text = f.read()

emails = re.findall(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", text,re.IGNORECASE)
phones = re.findall(r"(?:\+?\d{1,3}[-.\s]?)?\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b", text)
phones1 = re.findall(r"(?:\+?\d{1,3}?[\s])?\b\d{10}\b", text)

email=re.findall(r"[a-z0-9.+%-]+@[a-z0-9.-]+\.[a-z]{2,}",text,re.I)
dates = re.findall(r"\b\d{2}[:/-]\d{2}[/:-]\d{4}\b", text)

print("Emails:", emails)
print("ema:",email)
print("Phones:", phones)
print("Phones_country: ",phones1)
print("Dates:", dates)
# emails=re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}",text,re.ig)

email=re.findall(r"[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}",text,re.I) # normal
phone=re.findall(r"\b\d{10}\b",text)# normal indial phone no

print(phone)
print(email)