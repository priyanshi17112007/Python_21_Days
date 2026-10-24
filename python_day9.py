#---------------Introduction to Numpy--------------
""" Numpy stands for Numerical Python that is widely used for scientific comuting,data analysis,and numerical computing tasks
pip install numpy
in numpy,Array is fundamental object
Array is used to store homogeneous data element in contiguous block of memory
"""
import numpy as np #where np is alias
list1=[10,20,30,40]
array1=np.array(list1)
print(array1)
print(type(array1))

list2=[10,20.9,30,40]
array1=np.array(list2)
print(array1)

list3=[10,'p',30,40]
array1=np.array(list3)
print(array1)

list4=[10,20,30,40]
array1=np.array(list4,dtype=float)
print(array1)

list5=[10,20,30,40]#1-D array
array1=np.array(list5,dtype='U16')
print(array1)


import numpy as ny
list6=[[10,20,30],#2-D array
       [23,45,56],
       [99,90,33]]
array1=ny.array(list6)
print(array1.shape)
print(array1)

ar=np.array([[[10,20,30],[23,89,90]],
             [[44,55,66],[32,42,52]]])
print(array1.dtype)
print(ar.shape)
print(array1.itemsize)

arr=np.arange(1,8)
print(arr)

arr1=ny.arange(11,17).reshape((2,3))
print(arr1)


import numpy as ny
#arr2=ny.zeros(4)
arr2=ny.zeros((2,2))
arr3=ny.ones((2,2))
arr4=ny.ones(2,dtype=int)
print(arr2)
print(arr3)
print(arr4)

"""--------------Attributes of Numpy Array------------------------
1.ndim
2.shape
3.size
4.dtype
5.itemsize
"""
list3=[10,'p',30,40]
array1=np.array(list3)
print(array1.ndim)
print(array1.shape)
print(array1.size)
print(array1.dtype)
