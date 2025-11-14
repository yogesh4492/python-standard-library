"""append operations  its take the O(1) and its add from right end  or end of list"""
"""appendleft operation its take also O(1) and its add from left end or start of list"""


from collections import deque

list1=[11,20,30,40]

dq=deque(list1)

print(dq)
dq.append(10)
print(dq)
dq.appendleft(20)
print(dq)


