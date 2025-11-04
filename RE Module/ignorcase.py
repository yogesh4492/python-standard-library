#its match case ncensitive

import re
text="hello How Are You"
print(re.findall(r'Hello',text,re.IGNORECASE))
print(re.findall(r'how',text,re.I))