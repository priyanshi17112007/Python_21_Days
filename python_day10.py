#----------------indexing in Numpy Array------------------------
import numpy as np
arr1=np.array([10,20,30,50])
print(arr1[0])
print(arr1[-1])


array1 = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

print(array1[1, 2])
print(array1[0, :])
print(array1[:, 1])

#------------Slicing in numpy Array-------------------------------
Arr2=np.array([99,88,77,66,44])
print(Arr2[1:4])
print(Arr2[:])
print(Arr2[:-1])
print(Arr2[0:4:2])
print(Arr2[-3:-1:-1])
print(Arr2[::2])
print(Arr2[::-1])


import numpy as np
array1 = np.array([[15, 16, 17],
                   [25, 26, 27],
                   [35, 36, 37],
                   [45, 46, 47]])

print(array1[1, :])
print(array1[:, 1])
print(array1[1:3, 1:3])
print(array1[1:3, :])
print(array1[:, 1:3])
print(array1[1:3, 1])
print(array1[1:3, ::-1])

#---------------Arithmetic Operations in Numpy--------------------
import numpy as np

x = np.array([[1, 2],
              [3, 4]])
y = np.array([[11, 12],
              [13, 14]])
z = y * x
w = x+y
u = x-y
v=x @ y#matrix multiplication
t = y/x
s = y//x
e=y**x
m=y%x
print(z)
print(w)
print(u)
print(v)
print(t)
print(s)
print(e)
print(m)