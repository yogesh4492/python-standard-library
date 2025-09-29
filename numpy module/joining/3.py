import numpy as np

arr=np.array([1,2,3,4])
arr1=np.array([5,6,7,8])

arr2=np.stack((arr,arr1),axis=1)
print(arr2)