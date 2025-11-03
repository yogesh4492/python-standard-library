# import re
# txt="The rain in Spain"
# x=re.search("^The.*Spain$",txt)

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

import re
txt="hello how are yogesh"
x=re.search("^hello.*yogesh$",txt)
if x:
    print("Yes Available")
else:
    print("No Match")

    