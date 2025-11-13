""" deque : double ended queue is a means you can add and remove data from both ends
its do fifo and lifo both operation

----------------------------------------------------
It offers powerful built-in methods like appendleft(), popleft() and rotate().
----------------------------------------------------

append:it will add from right side  append the data means take O(1) times its mostly use for time complexity
appendleft: it will add from left side time complexity time(O(1))

pop: it will remove from right end
popleft : it will remove from left end


"""
from collections import deque

dq = deque([10, 20, 30])

# Add elements to the right
dq.append(40)  

# Add elements to the left
dq.appendleft(5)  

# extend(iterable)
dq.extend([50, 60, 70]) 
print("After extend([50, 60, 70]):", dq)

# extendleft(iterable)
dq.extendleft([0, 5])  
print("After extendleft([0, 5]):", dq)

# remove method
dq.remove(20)
print("After remove(20):", dq)

# Remove elements from the right
dq.pop()

# Remove elements from the left
dq.popleft()  

print("After pop and popleft:", dq)

# clear() - Removes all elements from the deque
dq.clear()  # deque: []
print("After clear():", dq)



