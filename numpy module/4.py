import numpy as np
arr=np.array([[1,3,5,5.0],[1,5,6,4]])#this work only if bot arry have same length
print(arr[0,1])#this print first array 2nd element

print(arr.ndim)
print(arr[0].dtype)