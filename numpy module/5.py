"""Slicing Array"""
import numpy as np

arr=np.array([1,2,3,4,5,6,7,8])
print(arr[:])
print(arr[1:5])
print(arr[:5])
print(arr[0:])
print(arr[::-1])
print(arr[::2])

print(arr[-3:-1][-1])